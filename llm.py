from google import genai
from google.genai import errors as genai_errors
from prompt import prompt_template
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"
client = None


def get_client():
    global client

    if client is None:
        api_key = os.getenv("GOOGLE_API_KEY", "").strip().strip("\"'")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env file or pass it to Docker with --env-file .env.")
        client = genai.Client(api_key=api_key)

    return client


def explain_genai_error(exc):
    message = str(exc)

    if "API_KEY_INVALID" in message or "API key n   ot valid" in message:
        return "GOOGLE_API_KEY is invalid. Create a valid Gemini API key and pass it with --env-file .env when running Docker."

    return f"Gemini request failed: {exc}"

def generate_result(query, relevant_docs):

    if not relevant_docs:
        return "I could not find relevant information in the video."

    prompt = prompt_template(query, relevant_docs)

    try:
        response = get_client().models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
    except genai_errors.ClientError as exc:
        raise ValueError(explain_genai_error(exc)) from exc

    return response.text
