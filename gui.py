from tkinter import *
from tkinter import filedialog
from parse import convert
import threading

def getResult(filename):
    convert(filename)

def getFile():
    global result
    filename = filedialog.askopenfilename()
    result = threading.Thread(target=getResult, args=(filename))
    return(result)

def mainGUI():
    global result
    root = Tk()

    imgButton = Button(command=getFile)
    imgButton.place(relx=.5, rely=.5, relwidth=.1, relheight=.1)

    submitButton = Button(command=root.destroy, text='Submit')
    submitButton.place(relx=.9, rely=.5, relwidth=.1, relheight=.1)

    root.mainloop()
    return(result)
