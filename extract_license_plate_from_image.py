#harcascades and yolov7
import cv2
import pytesseract
from PIL import Image, ImageFilter
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# def extract_license_plate_from_image(image_path, grayscale=True, blur=True, threshold=True, morph=True, 
#                                      canny=True, contour=True, ocr_engine='tesseract'):
def extract_license_plate_from_image(image_path):
  image=Image.open(image_path)
   
  text=pytesseract.image_to_string(image);
  print("License Plate Number : ",text)
  return text
"""
  Extracts the license plate number from an image.

  Args:
      image_path (str): Path to the image file.
      grayscale (bool, optional): Convert image to grayscale (default: True).
      blur (bool, optional): Apply Gaussian blur (default: True).
      threshold (bool, optional): Apply adaptive thresholding (default: True).
      morph (bool, optional): Apply morphological operations (default: True).
      canny (bool, optional): Apply Canny edge detection (default: True).
      contour (bool, optional): Find contours to isolate license plate (default: True).
      ocr_engine (str, optional): OCR engine to use (default: 'tesseract').

  Returns:
      str: The extracted license plate number, or None if no plate is found.
"""

  # Read the image
#   img = Image.open('image_path')
# #   Convert to grayscale
#   img=img.reduce(4)
#   img=img.convert('L')
#   img=img.filter(ImageFilter.BLUR)
#   img.save('p1_changes.jpg')
#   text = pytesseract.image_to_string(img)
#   return remove(text.strip())

  # Preprocessing (adjust parameters as needed)
#   if grayscale:
#       img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   if blur:
#       img = cv2.GaussianBlur(img, (5, 5), 0)
#   if threshold:
#       img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#   if morph:
#       kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#       img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#   if canny:
#       img = cv2.Canny(img, 50, 200)

#   # Find contours (adjust parameters as needed)
#   if contour:
#       contours, _ = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#       cnt = None  # Initialize plate contour variable

#       # Find the largest contour likely resembling a license plate
#       for c in contours:
#           peri = cv2.arcLength(c, True)
#           approx = cv2.approxPolyDP(c, 0.02 * peri, True)

#           if len(approx) == 4:  # Likely a rectangle (license plate shape)
#               cnt = approx
#               break

#       # Extract region of interest (ROI) if a contour is found
#       if cnt is not None:
#           x, y, w, h = cv2.boundingRect(cnt)
#           roi = img[y:y+h, x:x+w]
#       else:
#           return None  # No license plate found

#   # Apply OCR (adjust engine and parameters as needed)
#   text = None
#   if ocr_engine == 'tesseract':
#       try:
     # Treat image as single block of text
#       except:
#           pass  # Tesseract might not be installed or have errors
#   else:
#       # Add code for other OCR engines if desired

   
