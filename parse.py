from PIL import Image
import threading
import dateparser
import pytesseract
import re
import cv2

def convert(imgs):
    results = []
    for img in imgs:
        file = open('data/names.txt', 'r')
        names = []
        name = ''

        for line in file:
            names.append(line)

        for i in range(len(names)):
            names[i] = names[i].replace('\n', '')

        text = pytesseract.image_to_string(Image.open(img))
        print(text)
        date = re.search('[0-9][0-9]/[0-9][0-9]/[0-9]+', text)
        if(date == None):
            date = re.search('[0-9][0-9]\[0-9][0-9][0-9]\[0-9][0-9]+', text)
        if(date == None):
            date = 'Not found'

        price = re.findall('[0-9]+\.[0-9]+', text)
        if(price == None or price == []):
            price = 'Not found'

        for i in range(len(names)):
            if names[i] in text:
                name = names[i]
                break
            else:
                name = 'Not Found'
        results.append((date[0], price[-1], name))
        print(results)
    return(results)
