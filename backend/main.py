from fastapi import FastAPI
from backend.routes.rag import router

app = FastAPI(
    title="YouTube RAG API",
    description="API for asking questions about YouTube videos",
    version="1.0.0",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the YouTube RAG API!"
    }   