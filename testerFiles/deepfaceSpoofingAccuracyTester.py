import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helpers.getVectorEmbedding import getVectorEmbeddingFromLocalPhoto
from helpers.videoCapture import captureAndSaveFaces


def testdeepfaceSpoofingAccuracy(datasetPath):
    if not os.path.isdir(datasetPath):
        return {
            "result": "dataset path is incorrect"
        }

    truePositive = trueNegative = falsePositive = falseNegative = fileCount =  0
    for folderName in os.listdir(datasetPath):
        folderPath = os.path.join(datasetPath, folderName)
        if os.path.isdir(folderPath):
            for fileName in os.listdir(folderPath):
                filePath = os.path.join(folderPath, fileName)

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
                        if "spoof" in folderName:
                            falsePositive += 1 
                        else:
                            truePositive += 1
                    except ValueError:
                        if "spoof" in folderName:
                            trueNegative += 1
                        else:
                            falseNegative += 1
                else:
                    print("Unsupported file type.")
    print(f"true positive: {truePositive}")
    print(f"true negative: {trueNegative}")
    print(f"false positive: {falsePositive}")
    print(f"false negative: {falseNegative}")
    print(f"Total file count: {fileCount}")
    

