import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open Camera")
    exit()
while True:
    # screenshot guts
    screenshot = None
    # capture frame-by-frame 
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print(" Can't receive frame (stream end?). Exiting...")
        break
    # our operations is on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # dsiplay the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# when everything done, release the capture
cap.release()
cv.destroyAllWindows()