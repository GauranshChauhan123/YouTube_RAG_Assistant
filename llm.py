from google import genai
from prompt import prompt_template
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_NAME = "gemini-2.5-flash"
client = None


def get_client():
    global client

    if client is None:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY is missing. Add it to your .env file.")
        client = genai.Client(api_key=api_key)

    return client

def generate_result(query, relevant_docs):

    if not relevant_docs:
        return "I could not find relevant information in the video."

    prompt = prompt_template(query, relevant_docs)

    response = get_client().models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
