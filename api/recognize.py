from fastapi import FastAPI, APIRouter, File, UploadFile
from helpers import getVectorEmbedding
from database.database import lookupFace
router = APIRouter()



@router.post("/recognize")
async def recognize(image : UploadFile = File(...)):
    userEmbedding = getVectorEmbedding.getVectorEmbedding(image)

    topResult = lookupFace(userEmbedding)  

    if topResult:
        return {
            "status": "received",
            "userID": {topResult[0][1]},
            "username": {topResult[0][2]}, 
            "distance": {topResult[0][3]}
        }
    return {"status": "no user found"}