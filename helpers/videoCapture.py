import time
from typing import Optional
import cv2
import os
from deepface import DeepFace
from helpers import getVectorEmbedding
from database.database import lookupFace
def captureAndSaveFaces(
    source=0,
    savePath="CapturedFaces",
    detectorBackend="opencv",
    maxFaceFrames=10, 
    timeThreshold=10, 
    searchDatabase=True, 
    throwErrorForSpoofing=False
):
    cap = cv2.VideoCapture(source)
    os.makedirs(savePath, exist_ok=True)
    startTime = time.time()
    savedFacesCount = 0

    #Storing frames with faces locally
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            break
        try:
            DeepFace.extract_faces(frame)
            faceFileName = os.path.join(savePath, f"face_{savedFacesCount}.jpg") 
            cv2.imwrite(faceFileName, frame)
            savedFacesCount += 1
        except:
            pass
        if savedFacesCount >= maxFaceFrames:
            cap.release()
            cv2.destroyAllWindows()
            print(f"Done: {savedFacesCount} face(s) saved. Exiting.")
            break
        if time.time() - startTime >= timeThreshold:
            cap.release()
            cv2.destroyAllWindows()
            print(f"Timeout: {timeThreshold} seconds have passed.")
            break
        #delete if you don't want the stream showing
        #cv2.imshow("VideoFeed", frame)
        #if cv2.waitKey(1) & 0xFF == ord("q"):
            #break

    cap.release() 
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    #print(f"Stopped early. {savedFacesCount} face(s) saved.") 


    #Looking up the frames
    for i in range(savedFacesCount):
        try:
            embedding = getVectorEmbedding.getVectorEmbeddingFromLocalPhoto(os.path.join(savePath, f"face_{i}.jpg"))
        except ValueError:
            if throwErrorForSpoofing:
                raise ValueError("Spoofing detected")
            else:
                return {
                    "status": "spoofing attempt detected"
                } 
        if searchDatabase:
            result = lookupFace(embedding)

            if result:
                return {
                "status": "received",
                "userID": {result[0][1]},
                "username": {result[0][2]}, 
                "distance": {result[0][3]}
            }
    if searchDatabase:
        return {
            "status": "user not found" 
        }
    return



