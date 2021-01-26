from PIL import Image
import threading
import dateparser
import pytesseract
import re
import cv2

def convert(imgs):
    results = []

    # Loop through images in user input
    for img in imgs:
        # Open names file to get all store names
        file = open('data/names.txt', 'r')
        names = []
        name = ''

        # Loop through lines in name file
        for line in file:
            names.append(line)

        # Parse names data
        for i in range(len(names)):
            names[i] = names[i].replace('\n', '')

        # Read text on users image
        text = pytesseract.image_to_string(Image.open(img))
        print(text)

        # Extract date from image
        date = re.search('[0-9][0-9]/[0-9][0-9]/[0-9]+', text)
        if(date == None):
            date = re.search('[0-9][0-9]\[0-9][0-9][0-9]\[0-9][0-9]+', text)
        if(date == None):
            date = 'N'

        # Extract price from image
        price = re.findall('[0-9]+\.[0-9]+', text)
        if(price == None or price == []):
            price = 'N'

        # Extract store name from image
        for i in range(len(names)):
            if names[i] in text:
                name = names[i]
                break
            else:
                name = 'Not Found'

        # Add parsed information to results variable
        results.append((date[0], price[-1], name))
        print(results)
    return(results)
