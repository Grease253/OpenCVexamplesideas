import cv2 as cv
import sys

img = cv.imread(cv.samplesfindFile("testimg.jpg"))

if img is none:
    sys.exit("Could not read the image")
cv.imshow("Display window", img)
k = cv.waitkey(0)

if k == ord("s"):
    cv.imwrite("testimg.png", img)