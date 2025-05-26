from deepface import DeepFace
import os
import shutil

def getVectorEmbedding(image):
    imagePath = f"tempImages/temp.jpg"
    with open(imagePath, "wb") as f:
        shutil.copyfileobj(image.file, f)
    userEmbedding = DeepFace.represent(img_path=imagePath)
    try:
        os.remove(imagePath)
    except FileNotFoundError:
        pass  # Optional: log a warning or ignore silently


    return userEmbedding[0]['embedding']