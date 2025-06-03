from fastapi import FastAPI, APIRouter
from deepface import DeepFace
from helpers import videoCapture
router = APIRouter()


@router.get("/stream")
async def stream():
    return videoCapture.captureAndSaveFaces()




