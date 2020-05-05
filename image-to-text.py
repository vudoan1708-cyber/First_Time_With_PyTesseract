# import tesseract 
import pytesseract as pt

# link to Tesseract installation: 
# https://github.com/UB-Mannheim/tesseract/wiki?fbclid=IwAR2aj_N_2qrLLyNFRYwULr_1NDaB20TPQa93h-beGDvIQv1akGsByEXYCOQ

# then add tesseract to the path
# pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# import python imaging library
from PIL import Image

import cv2 as cv

# import numpy as np

langs = 'vie+eng+kor+chi_sim+fra+jpn'
# img = Image.open('media/img/3.jpg')
cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Live Webcam', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    toText = pt.image_to_string(gray, lang=langs)
    if toText == '' or toText == None:
        pass
    else:
        print(toText)

# able to run and detect SOME text, but because of really high latency (lagging), it's hard for OCR to recognise live webcam

# testing for other languages with still images (SUCCEEDED)
# langs = 'vie+eng+kor+chi_sim+fra'
# img = Image.open('media/img/fra.png')
# toText = pt.image_to_string(img, lang=langs)
# print(toText)