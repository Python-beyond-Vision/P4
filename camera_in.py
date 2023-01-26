import sys
import cv2

cap = cv2.VideoCapture('Video/vtest.avi')

if not cap.isOpened():
    print('camera open failed')
    sys.exit()
    
# Test
while True:
    ret, frame = cap.read()

    
    
    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) == 27:
        break

cap.release()