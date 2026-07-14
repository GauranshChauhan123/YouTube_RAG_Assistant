from pydantic import BaseModel, Field


class AskQuestionResponse(BaseModel):
    success: bool
    video_id: str
    answer: str