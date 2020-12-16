from tkinter import *
from tkinter import filedialog
from parse import convert
import threading

def getFile():
    global result
    filename = filedialog.askopenfilename()
    result = convert(filename)
    result = str(result).replace('(', '')
    result = result.replace(')', '')
    result = result.replace("'", '')
    addInfo(result)
    print(result)

def mainGUI():
    global result
    global parsedText
    root = Tk()
    root.geometry('600x400')
    root.configure(background='light gray')

    parsedText = StringVar()
    parsedInfo = Entry(textvariable=parsedText, font='Helvecta 25')
    parsedInfo.place(relx=.1, rely=.5, relwidth=.8, relheight=.2)

    imgButton = Button(command=getFile, text='Upload', bg='dark gray')
    imgButton.place(relx=.375, rely=.2, relwidth=.25, relheight=.15)

    submitButton = Button(command=root.destroy, text='Submit', bg='dark gray')
    submitButton.place(relx=.4, rely=.8, relwidth=.2, relheight=.1)

    root.mainloop()
    return(result)

def addInfo(result):
    global parsedText
    parsedText.set(str(result))
