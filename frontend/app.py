import requests
import streamlit as st
import os

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

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/rag/ask")



st.set_page_config(
    page_title="YouTube RAG Assistant",
    page_icon="🎥",
)

st.title("🎥 YouTube RAG Assistant")

video_url = st.text_input("YouTube Video URL")

language = st.selectbox(
    "Transcript Language",
    options=list(LANGUAGE_OPTIONS.keys()),
)

question = st.text_area("Ask a question")

if st.button("Get Answer"):

    if not video_url or not question:
        st.warning("Please enter both the video URL and a question.")
        st.stop()

    payload = {
        "video_url": video_url,
        "question": question,
        "language": language,
    }

    with st.spinner("Generating answer..."):

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                data = response.json()

                st.success("Answer generated successfully!")

                st.write("### Answer")
                st.write(data["answer"])

            else:
                st.error(response.json()["detail"])

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the FastAPI server.")