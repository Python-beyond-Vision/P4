import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

template = cv2.imread('image/pattern_eye.jpg')
height, width = template.shape[:2]

while True:
    ret, frame = capture.read()
    # cv2.imshow("VideoFrame", frame)

    key = cv2.waitKey(10)   # 'q' pressed
    if key == 113:
        print('pressed')
        cv2.imwrite("roi2.jpg", frame)

    elif key > 10:
        break

    for method in methods:
        result = cv2.matchTemplate(frame, template, eval(method))
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if method in ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']:
            top_left = min_loc
        else:
            top_left = max_loc

        bottom_right = (top_left[0] + width, top_left[1] + height)

        cv2.rectangle(frame, top_left, bottom_right, (0, 0, 225), 2)
        cv2.imshow(method, frame)


capture.release()
cv2.destroyAllWindows()




# def mouse_event(event, x, y, flags, param):
#     global clicked_x, clicked_y

#     if event == cv2.EVENT_LBUTTONDOWN:
#         clicked_x = x
#         clicked_y = y

#         cv2.putText(param, f"{x}, {y}", (x, y), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
#         cv2.imshow("draw", src)
#         print("MouseLBUTTONDOWN")

#     if event == cv2.EVENT_LBUTTONUP:
#         cv2.rectangle(param, (clicked_x, clicked_y), (x, y), (0, 255, 0), 2)
#         cv2.putText(param, f"{x}, {y}", (x, y), cv2.FONT_ITALIC, 1, (0, 0, 255), 2)
#         cv2.imshow("draw", src)
#         print("MouseLBUTTONUP")

#         # cut roi
#         roi = templit[clicked_y:y, clicked_x:x].copy()
#         cv2.imshow("roi", roi)
#         cv2.imwrite("roi.jpg", roi)
    
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     src = dst[:].copy()
    #     cv2.imshow("draw", src)
    #     print("MouseRBUTTONDOWN")

# src = cv2.imread("Image/MatchingTest/pattern.bmp", cv2.IMREAD_GRAYSCALE)
# templit = cv2.imread("roi.jpg", cv2.IMREAD_GRAYSCALE)
# dst = cv2.imread("Image/MatchingTest/pattern.bmp")



