from tkinter import *
from tkinter import filedialog
from parse import convert
import threading

def getFile():
    global result
    filename = filedialog.askopenfilename()
    result = convert(filename)
    print(result)

def mainGUI():
    global result
    root = Tk()

    imgButton = Button(command=getFile)
    imgButton.place(relx=.5, rely=.5, relwidth=.1, relheight=.1)

    submitButton = Button(command=root.destroy, text='Submit')
    submitButton.place(relx=.9, rely=.5, relwidth=.1, relheight=.1)

    root.mainloop()
    return(result)
