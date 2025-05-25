from fastapi import FastAPI, APIRouter, File, UploadFile, Form
from deepface import DeepFace
import shutil
router = APIRouter()

#TODO: for now only using one image per user, for more accuracy do more.
@router.post("/register")
async def addFace(image : UploadFile = File(...), userID: int = Form(...)):
    imagePath = f"tempImages/{userID}_temp.jpg"
    with open(imagePath, "wb") as f:
        shutil.copyfileobj(image.file, f)
    
    userEmbedding = DeepFace.represent(img_path=imagePath)
    print(userEmbedding)
    return {
        "status": "received",
        "employeeID": userID,
    }


