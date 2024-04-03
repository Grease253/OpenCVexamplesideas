import cv2 as cv
import numpy as np
import pytesseract
import pyautogui
# Initialize VideoCapture
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Read the first frame
ret, frame = cap.read()



# Define ROI for OCR
x1, y1, x2, y2 = 50, 50, 200, 200
roi = cv.rect(x1, y1, x2 - x1 + 1, y2 - y1 + 1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Display the frame in a window
    cv.imshow('Frame', frame)

    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Apply OCR using Tesseract (ROI only)
    text = pytesseract.image_to_string(gray, roi=roi)
    
    # Check if text has been detected
    if text:
        # Print the detected text
        print("Detected text:", text)
        
        # Simulate a keyboard key press (e.g., "t")
        pyautogui.keydown('`')
        pyautogui.keyup('`')
    
    # Wait for a key press
    cv2.waitKey(0)


# Release resources
cap.release()
cv.destroyAllWindows()
print('Done.')