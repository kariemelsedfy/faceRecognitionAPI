import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from helpers.getVectorEmbedding import getConfidenceLevelFromLocalPhoto

def displayFolderConfidenceLevels(folderPath:str):
    if os.path.isdir(folderPath):
        for img in os.listdir(folderPath):
            print(getConfidenceLevelFromLocalPhoto(os.path.join(folderPath, img)))

