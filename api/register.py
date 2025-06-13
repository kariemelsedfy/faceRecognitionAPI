from fastapi import FastAPI, APIRouter, File, UploadFile, Form
from deepface import DeepFace
from database.database import insertEmbedding
from helpers.getVectorEmbedding import getVectorEmbedding
import shutil
router = APIRouter()

#TODO: for now only using one image per user, for more accuracy do more.
@router.post("/register")
async def addFace(image : UploadFile = File(...), userID: int = Form(...), username: str = Form(...)):
    
    userEmbedding = getVectorEmbedding(image)

    insertEmbedding(userID, userEmbedding, username)
    return {
        "status": "received",
        "employeeID": userID,
        "username": username
    }


