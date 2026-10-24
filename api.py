
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from core.assistant import chat
from voice.speech_to_text import listen
from voice.text_to_speech import speak

app = FastAPI(title="AI Voice + Chat Assistant")



BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


class ChatRequest(BaseModel):
    message: str


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Assistant backend is running"}


@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    try:
        response = chat(message)
        return {"reply": response}
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Failed to get an AI response."
        ) from error


@app.post("/api/voice")
def voice_endpoint():
    try:
        user_message = listen()

        if not user_message:
            return {
                "user_message": None,
                "reply": "I couldn't understand that. Please try again."
            }

        response = chat(user_message)
        speak(response)

        return {
            "user_message": user_message,
            "reply": response
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail="Voice request failed."
        ) from error
