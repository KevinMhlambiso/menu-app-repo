from tkinter import *
from tkinter import filedialog
import subprocess
import platform

def openFile():
    filepath = filedialog.askopenfilename(initialdir="",title="open yo file",filetypes=(("text file","*.txt"),("all file","*-*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

def saveFile():
    file = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("text file",".txt"),("HTML file",".HTML"),("all files",".*")])
    # file.write(fileText)
    # fileText = input("enter text: ")
    # fileText = str(text.get(1.0,END))
    file.close()


def cutFile(source, destination):
    system = platform.system()
    if system == 'Windows':
        subprocess.run(['move', source, destination], shell=True, check=True)
    else:
        subprocess.run(['mv', source, destination], check=True)


source = 'path/to/source/file.txt'
destination = 'path/to/destination/file.txt'

cutFile(source, destination)
print(f"File moved from {source} to {destination}")


def copyFile(source, destination):
    system = platform.system()
    if system == 'Windows':
        subprocess.run(['copy', source, destination], shell=True, check=True)
    else:
        subprocess.run(['cp', source, destination], check=True)


source = 'path/to/source/file.txt'
destination = 'path/to/destination/file.txt'
copyFile(source, destination)



def pasteFile(source, destination):
    system = platform.system()
    if system == 'Windows':
        subprocess.run(['copy', source, destination], shell=True, check=True)
    else:
        subprocess.run(['cp', source, destination], check=True)


source = 'path/to/source/file.txt'
destination = 'path/to/destination/file.txt'

pasteFile(source, destination)
print(f"File pasted from {source} to {destination}")


windows = Tk()

fileImage = PhotoImage(file="file.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")
cutImage = PhotoImage(file="cut.png")
copyImage = PhotoImage(file="copy.png")
pasteImage = PhotoImage(file="paste.png")

menubar = Menu(windows)
windows.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",menu=fileMenu)
fileMenu.add_command(label="open",command=openFile,image=fileImage,compound='left')
fileMenu.add_command(label="save",command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="exit",command=quit,image=exitImage,compound='left')

editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="cut",command=cutFile,image=cutImage,compound='right')
editMenu.add_command(label="copy",command=copyFile,image=copyImage,compound='right')
editMenu.add_command(label="paste",command=pasteFile,image=pasteImage,compound='right')

windows.mainloop()
