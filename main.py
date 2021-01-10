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

result = mainGUI()

img = 'test3.jpg'

result = result.replace('(', '')
result = result.replace(')', '')
result = result.split(',')

print(addReceipt(result))
