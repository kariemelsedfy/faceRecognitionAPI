from fastapi import FastAPI, APIRouter, File, UploadFile
from helpers.getVectorEmbedding import getVectorEmbedding
from deepface.modules.verification import find_distance, find_threshold

router = APIRouter()


@router.post("/compareTwoImages")
async def compareTwoImages(image1 : UploadFile = File(...), image2 : UploadFile = File(...)):
    embedding1, embedding2 = getVectorEmbedding(image1), getVectorEmbedding(image2)
    distanceBetweenEmbeddings = find_distance(embedding1, embedding2, 'euclidean_l2')
    threshold = find_threshold(model_name='VGG-Face', distance_metric='euclidean_l2')
    if distanceBetweenEmbeddings <= threshold:
        return {
            "result": True,
            "status": "Images match",
            "distance": distanceBetweenEmbeddings,
            "threshold": threshold
        }
    return {
        "result": False,
        "status": "Images do not match", 
        "distance": distanceBetweenEmbeddings, 
        "threshold": threshold
    }