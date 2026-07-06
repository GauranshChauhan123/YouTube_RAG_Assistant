import re
from urllib.parse import parse_qs, urlparse

import streamlit as st


LANGUAGE_OPTIONS = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Portuguese": "pt",
    "Arabic": "ar",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
}


st.set_page_config(
    page_title="YouTube RAG Assistant",
    page_icon="",
    layout="centered",
)


def extract_video_id(video_input: str) -> str:
    """Return a YouTube video id from either a raw id or a common YouTube URL."""
    video_input = video_input.strip()

    if not video_input:
        return ""

    if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_input):
        return video_input

    parsed = urlparse(video_input)

    if parsed.hostname in {"youtu.be", "www.youtu.be"}:
        return parsed.path.strip("/")[:11]

    if parsed.hostname in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        query_video_id = parse_qs(parsed.query).get("v", [""])[0]
        if query_video_id:
            return query_video_id[:11]

        path_parts = [part for part in parsed.path.split("/") if part]
        if len(path_parts) >= 2 and path_parts[0] in {"embed", "shorts"}:
            return path_parts[1][:11]

    return video_input


def process_video(video_id: str, language: str):
    from input_transcript import fetch_transcript
    from split_transcript import split_transcript
    from vector_store import create_vector_store

    transcript = fetch_transcript(video_id, language)

    if not transcript:
        raise ValueError("Could not fetch a transcript for this video and language.")

    chunks = split_transcript(transcript)

    if not chunks:
        raise ValueError("Transcript was fetched, but no chunks were created.")

    create_vector_store(chunks, video_id)
    return len(chunks)


st.title("YouTube RAG Assistant")

with st.sidebar:
    st.header("Video")
    video_input = st.text_input(
        "YouTube URL or video ID",
        placeholder="https://www.youtube.com/watch?v=...",
    )
    selected_transcript_language = st.selectbox(
        "Transcript/captions language",
        options=list(LANGUAGE_OPTIONS.keys()),
        index=0,
    )
    language_code = LANGUAGE_OPTIONS[selected_transcript_language]
    process_clicked = st.button("Process video", type="primary", use_container_width=True)

if "video_id" not in st.session_state:
    st.session_state.video_id = ""

if process_clicked:
    video_id = extract_video_id(video_input)

    if not video_id:
        st.sidebar.error("Please enter a YouTube URL or video ID.")
    else:
        with st.spinner("Fetching transcript and building vector store..."):
            try:
                chunk_count = process_video(video_id, language_code)
                st.session_state.video_id = video_id
               # st.sidebar.success(f"Ready. Stored {chunk_count} chunks.")
            except Exception as exc:
                st.session_state.video_id = ""
                st.sidebar.error(str(exc))

active_video_id = st.session_state.video_id or extract_video_id(video_input)

if active_video_id:
    st.caption(f"Active video ID: `{active_video_id}`")
else:
    st.info("Add a YouTube URL or video ID in the sidebar, then process the video.")

query = st.text_area(
    "Ask a question about the video",
    placeholder="What are the main points explained in this video?",
    height=100,
)

ask_clicked = st.button(
    "Generate answer",
    type="primary",
    disabled=not bool(active_video_id and query.strip()),
)

if ask_clicked:
    with st.spinner("Searching the transcript and asking Gemini..."):
        from llm import generate_result
        from retrieve import retrieve_related_info

        try:
            relevant_docs = retrieve_related_info(
                query=query.strip(),
                video_id=active_video_id,
            )
            answer = generate_result(query.strip(), relevant_docs)
        except Exception as exc:
            st.error(str(exc))
            st.stop()

    st.subheader("Answer")
    st.write(answer)
