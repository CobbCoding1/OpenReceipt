from gui import mainGUI
from parse import convert
from excel import addReceipt
from PIL import Image
import threading
import dateparser
import pytesseract
import re
import cv2

filename = ''
results = []

result = mainGUI()

img = 'test3.jpg'

result = result.split('),')

for i in result:
    i = i.replace('(', '')
    i = i.replace(')', '')
    i = i.split(',')
    results.append(addReceipt(i))

#result = result.replace('(', '')
#result = result.replace(')', '')
#result = result.split(',')

print(results)
