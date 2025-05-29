import os, sys
from helpers.getVectorEmbedding import getVectorEmbeddingFromLocalPhoto
from database import insertEmbedding
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

celebrityDataSetPath = "CelebrityFacesDataSet"


celebrityID = 0 
for celebrityFolder in os.listdir(celebrityDataSetPath):

    celebrityFolderPath = os.path.join(celebrityDataSetPath, celebrityFolder)


    if os.path.isdir(celebrityFolderPath):

        for image in os.listdir(celebrityFolderPath):
            imagePath = os.path.join(celebrityFolderPath, image)
            imageEmbedding = getVectorEmbeddingFromLocalPhoto(imagePath)

            insertEmbedding(celebrityID, imageEmbedding, celebrityFolder)
        os.rename(celebrityFolderPath, celebrityFolderPath + str(celebrityID))

    celebrityID+=1

        