from deepface import DeepFace
from fastapi import UploadFile
import os
import shutil

def getVectorEmbedding(image: UploadFile):
    imagePath = f"tempImages/temp.jpg"
    with open(imagePath, "wb") as f:
        shutil.copyfileobj(image.file, f)
    userEmbedding = DeepFace.represent(img_path=imagePath, enforce_detection=False)
    try:
        os.remove(imagePath)
    except FileNotFoundError:
        pass  # Optional: log a warning or ignore silently

    return userEmbedding[0]['embedding']


def getVectorEmbeddingFromLocalPhoto(imagePath: str):
    userEmbedding = DeepFace.represent(img_path=imagePath, enforce_detection=False)
    return userEmbedding[0]['embedding']


def getConfidenceLevelFromLocalPhoto(imagePath:str):
    userEmbedding = DeepFace.represent(img_path=imagePath, enforce_detection=False)
    return userEmbedding[0]['face_confidence']


