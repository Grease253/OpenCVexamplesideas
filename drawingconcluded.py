import numpy as np
import cv2 as cv

# create a black image
img = np.zeros((512,512,3), np.uint8)

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# draw a diagonal blue line with thickness of 5px
cv.line(img,(0,0),(511,511),(255,0,0),5)

cv.circle(img,(447,63), 63, (0,0,255), -1)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)