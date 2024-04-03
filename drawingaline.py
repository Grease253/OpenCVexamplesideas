import numpy as np
import cv2 as cv

# create a black image
img = np.zeros((512,512,3), np.uint8)

# draw a diagonal blue line with thickness of 5px
cv.line(img,(0,0),(511,511),(255,0,0),5)