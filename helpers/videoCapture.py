import cv2
import os
from deepface import DeepFace
from helpers import getVectorEmbedding
from database import lookupFace
def grabFacialAreas(img, detectorBackend="opencv", threshold=130):
    try:
        faceObjs = DeepFace.extract_faces(
            img_path=img,
            detector_backend=detectorBackend,
            expand_percentage=0,
            enforce_detection=False
        )
        faces = [
            (
                faceObj["facial_area"]["x"],
                faceObj["facial_area"]["y"],
                faceObj["facial_area"]["w"],
                faceObj["facial_area"]["h"]
            )
            for faceObj in faceObjs
            if faceObj["facial_area"]["w"] > threshold
        ]
        return faces
    except:
        return []

def extractFacialAreas(img, facesCoordinates):
    detectedFaces = []
    for x, y, w, h in facesCoordinates:
        faceImg = img[y : y + h, x : x + w]
        detectedFaces.append(faceImg)
    return detectedFaces

# --- Main Function ---    

def captureAndSaveFaces(
    source=0,
    savePath="CapturedFaces",
    detectorBackend="opencv",
    maxFaceFrames=10
):
    cap = cv2.VideoCapture(source)
    os.makedirs(savePath, exist_ok=True)

    savedFacesCount = 0

    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            break

        faces = grabFacialAreas(frame, detectorBackend=detectorBackend)
        faceImages = extractFacialAreas(frame, faces)
        if len(faceImages) > 0:
            faceFileName = os.path.join(savePath, f"face_{savedFacesCount}.jpg") 
            cv2.imwrite(faceFileName, frame)
            savedFacesCount += 1
        
            if savedFacesCount >= maxFaceFrames:
                cap.release()
                cv2.destroyAllWindows()
                print(f"Done: {savedFacesCount} face(s) saved. Exiting.")
                return
        #delete if you don't want the stream showing
        cv2.imshow("VideoFeed", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    print(f"Stopped early. {savedFacesCount} face(s) saved.") 
