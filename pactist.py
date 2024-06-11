from tkinter import *
from tkinter import filedialog

# def click():

def saveFile():
    file = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("text file",".txt"),("HTML file",".HTML"),("all files",".*")])
    file.write(filetext)
    filetext = input("enter text: ")
    filetext = str(text.get(1.0,END))
    file.close()
 
windows = Tk()


text = Text(windows)
text.pack()

button = Button(windows,command=saveFile,text='open')
button.pack()

windows.mainloop()