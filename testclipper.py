import cv2
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
import os
os.environ["TESSDATA_PREFIX"] = "/path/to/tesseract/tessdata"

# Read the image from which text needs to be extracted
image = cv2.imread("image.png")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform text detection on each frame using Tesseract OCR
text = pytesseract.image_to_string(gray)

# Display the detected text
cv2.imshow("Text", text)
cv2.waitKey(0)