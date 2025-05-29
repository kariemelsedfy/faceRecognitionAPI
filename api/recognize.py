from fastapi import FastAPI, APIRouter, File, UploadFile
from helpers import getVectorEmbedding
from database import lookupFace
router = APIRouter()



@router.post("/recognize")
async def recognize(image : UploadFile = File(...)):
    userEmbedding = getVectorEmbedding.getVectorEmbedding(image)

    userID = lookupFace(userEmbedding)  

    return {
        "status": "received",
        "userID": {userID}
    }