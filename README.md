# YouTube RAG Assistant

A Streamlit app that lets you ask questions about a YouTube video using its transcript/captions. The app fetches the selected transcript language, chunks the transcript, stores embeddings in Chroma, retrieves relevant context, and uses Gemini to generate an answer.

## Features

- Accepts a YouTube URL or video ID.
- Lets users select the transcript/captions language.
- Builds a local Chroma vector store from the transcript.
- Answers questions using retrieved transcript context.
- Keeps retrieved chunks hidden from the answer UI.

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

## Run

```powershell
streamlit run app.py
```

Then open the local URL shown by Streamlit, usually:

```text
http://localhost:8501
```

## Usage

1. Paste a YouTube URL or video ID in the sidebar.
2. Select the transcript/captions language.
3. Click **Process video**.
4. Ask a question about the video.
5. Click **Generate answer**.

## Project Structure

- `app.py` - Streamlit UI and app flow.
- `input_transcript.py` - Fetches YouTube transcripts.
- `split_transcript.py` - Splits transcript text into chunks.
- `vector_store.py` - Creates the Chroma vector store.
- `retrieve.py` - Retrieves relevant transcript chunks.
- `prompt.py` - Builds the LLM prompt.
- `llm.py` - Calls the Gemini model.
- `utils.py` - Shared embedding helper.

## Notes

- The selected language must be available as captions/transcript for the YouTube video.
- Generated local data is stored in `chroma_db/`.
- Secrets and local generated files are ignored by `.gitignore`.
