from fastapi import FastAPI, APIRouter, File, UploadFile
from deepface import DeepFace
from helpers import getVectorEmbedding, getFaceRecognitionQuery
from database import lookupFace
router = APIRouter()



@router.post("/recognize")
async def recognize(image : UploadFile = File(...)):
    userEmbedding = getVectorEmbedding.getVectorEmbedding(image)
    findUserQuery = getFaceRecognitionQuery.getFaceRecognitionQuery


    userID = lookupFace(userEmbedding)

    return {
        "status": "received",
        "userID": {userID}
    }