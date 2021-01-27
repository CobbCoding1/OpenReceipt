from tkinter import *
from tkinter import filedialog
from excel import open_file
from parse import convert
import threading

def getFile():
    global result
    # Ask for filename from user
    filename = filedialog.askopenfilename(multiple=True)
    print(filename)
    # Parse results to remove bloat
    result = convert(filename)
    result = str(result).replace("'", '')
    result = result.replace('[', '')
    result = result.replace(']', '')

    # Set the display to the result
    addInfo(result)
    print(result)

def mainGUI():
    global result
    global parsedText
    global root

    # Create the main GUI
    root = Tk()
    root.geometry('600x400')
    root.configure(background='light gray')

    # Add entry for result
    parsedText = StringVar()
    parsedInfo = Entry(textvariable=parsedText, font='Helvecta 25')
    parsedInfo.place(relx=.1, rely=.5, relwidth=.8, relheight=.2)

    # Add button for getting the image from user
    imgButton = Button(command=getFile, text='Upload', bg='dark gray')
    imgButton.place(relx=.375, rely=.2, relwidth=.25, relheight=.15)

    # Add submit button to send results to excel file
    submitButton = Button(command=submit, text='Submit', bg='dark gray')
    submitButton.place(relx=.4, rely=.8, relwidth=.2, relheight=.1)

    # Create excel file button
    excelButton = Button(command=load_file, text='Load excel file', bg='dark gray')
    excelButton.place(relx=.4, rely=.05, relwidth=.2, relheight=.1)

    # Mainloop
    root.mainloop()
    return(result)

def submit():
    global result
    global parsedText
    global root

    # Get text from input box
    result = parsedText.get()

    # Destroy window
    root.destroy()

def addInfo(result):
    global parsedText
    parsedText.set(str(result))

def load_file():
    filename2 = filedialog.askopenfilename()
    open_file(filename2)
