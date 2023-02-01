import cv2
import numpy as np

capture = cv2.VideoCapture(0)

faceCascadePath = '/Users/eungushin/Documents/Git/opencv-1/data/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(faceCascadePath)

while True:
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

    ret, frame = capture.read()
    image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(image_gray, scaleFactor=1.1,
                                                    minNeighbors=5,
                                                    minSize=(150,150))

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (127,255,0), 3)

    
    cv2.imshow("VideoFrame", frame)


capture.release()
cv2.destroyAllWindows()