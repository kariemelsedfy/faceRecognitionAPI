import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helpers.getVectorEmbedding import getVectorEmbeddingFromLocalPhoto
from helpers.videoCapture import captureAndSaveFaces


def testdeepfaceSpoofingAccuracyOnAllSpoofDataSet(datasetPath):
    if not os.path.isdir(datasetPath):
        return {
            "result": "dataset path is incorrect"
        }

    fileCount = spoofingDetected = 0
    for fileName in os.listdir(datasetPath):
        filePath = os.path.join(datasetPath, fileName)

        # ✅ Get file extension
        _, file_extension = os.path.splitext(fileName)

        print(f"File: {fileName}, Extension: {file_extension}")
        fileCount += 1
        if file_extension.lower() in ['.jpg', '.jpeg', '.png']:
            try:
                getVectorEmbeddingFromLocalPhoto(filePath)
                truePositive += 1
            except ValueError:
                falseNegative += 1
        elif file_extension.lower() in ['.mp4', '.avi', '.mov']:
            try:
                captureAndSaveFaces(source=filePath, searchDatabase=False, throwErrorForSpoofing=True)
            except ValueError:
                spoofingDetected += 1
        else:
            print("Unsupported file type.")
   
    print(f"Total file count: {fileCount}")
    print(f"Accuracy: {spoofingDetected/fileCount}")


testdeepfaceSpoofingAccuracyOnAllSpoofDataSet("/Users/kelsedfy/Library/CloudStorage/OneDrive-BowdoinCollege/Desktop/faceRecognitionAPI/spoofVideo/files")