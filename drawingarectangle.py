import numpy as np
import cv2 as cv

# create a black image
img = np.zeros((512,512,3), np.uint8)

cv.rectangle(img,(384,0),(510,128),(0,255,0),3)