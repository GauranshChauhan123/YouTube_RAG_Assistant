from fastapi import APIRouter
from backend.services.rag_service import ask_question
from backend.models.request_model import AskQuestionRequest
from backend.models.response_model import AskQuestionResponse
from fastapi import HTTPException


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

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "YouTube RAG API is running."
    }

@router.post('/ask')
def ask(request:AskQuestionRequest,response_model=AskQuestionResponse):

    language = LANGUAGE_OPTIONS[request.language]

    try:

        return ask_question(request=request,language=language)
    
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
