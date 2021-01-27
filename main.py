from gui import mainGUI
from parse import convert
from excel import addReceipt
from PIL import Image
import threading
import dateparser
import pytesseract
import re
import cv2
import os

# Declare tesseract exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Check if filename.txt exists, if not create it
if(os.path.isfile('filename.txt')):
    pass
else:
    f = open('filename.txt', 'w')

# Declare variables
filename = ''
results = []

# Get the result & open GUI by calling GUI function
result = mainGUI()

# Convert result to list
result = result.split('),')

# Loop through all files selected
for i in result:
    i = i.replace('(', '')
    i = i.replace(')', '')
    i = i.split(',')
    results.append(addReceipt(i))

# Print output
print(results)
