from pydantic import BaseModel, Field
from typing import Annotated



class AskQuestionRequest(BaseModel):
    video_url: str = Field(
        ...,
        description="YouTube video URL"
    )
    question: str = Field(
        ...,
        min_length=1,
        max_length=500,
        description="Question to ask about the video"
    )
    
    language : str  = Field(
        ..., 
        description="language of the transcript/captions"
    ) 

