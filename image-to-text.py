# import tesseract 
import pytesseract as pt

# link to Tesseract installation: 
# https://github.com/UB-Mannheim/tesseract/wiki?fbclid=IwAR2aj_N_2qrLLyNFRYwULr_1NDaB20TPQa93h-beGDvIQv1akGsByEXYCOQ

# then add tesseract to the path
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# import python imaging library
from PIL import Image

# import opencv
import cv2 as cv

# import numpy as np
# print('Package Loaded')
# img = Image.open('media/img/3.jpg')
cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()
    cv.imshow('Live Webcam', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    toText = pt.image_to_string(img)
    if toText == '' or toText == None:
        pass
    else:
        print(toText)

