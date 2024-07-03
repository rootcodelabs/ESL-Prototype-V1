from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from api.services import generate_avatar, iterfile
from util import preprocess_phrase

router = APIRouter()

class PhraseRequest(BaseModel):
    phrase: str

@router.post("/generate_video")
async def generate_video(request: PhraseRequest):
    phrase = request.phrase
    words = preprocess_phrase(phrase)
    if not words:
        raise HTTPException(status_code=400, detail="Invalid phrase")

    file_path = generate_avatar(words=words)
    return StreamingResponse(iterfile(file_path), media_type="video/mp4")
