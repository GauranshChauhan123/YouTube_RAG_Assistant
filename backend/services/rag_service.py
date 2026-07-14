from backend.models.request_model import AskQuestionRequest
from backend.models.response_model import AskQuestionResponse
from backend.utils.id_extractor import extract_video_id
from backend.services.input_transcript import fetch_transcript
from backend.services.split_transcript import split_transcript
from backend.services.vector_store import create_vector_store
from backend.services.retrieve import retrieve_related_info
from backend.services.prompt import prompt_template
from backend.services.llm import generate_result
from fastapi import HTTPException


def ask_question(request:AskQuestionRequest,language:str)-> AskQuestionResponse:
    video_id= extract_video_id(request.video_url)
    question=request.question.strip()

   
    transcript=fetch_transcript(video_id,language)

    if not transcript:
      raise ValueError("Could not fetch a transcript for this video and language.")


    chunks = split_transcript(transcript)

    if not chunks:
      raise ValueError("Transcript was fetched, but no chunks were created.")

    create_vector_store(chunks,video_id)

    relevant_docs=retrieve_related_info(question,video_id,k=5)
    
    answer = generate_result(question,relevant_docs)

    return AskQuestionResponse(
        success=True,
        video_id=video_id,
        answer=answer
    )
    














