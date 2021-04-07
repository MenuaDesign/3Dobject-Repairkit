from tkinter import *
import tkinter as tk
from tkinter import filedialog
from System import *
file = ""

def gui():
    root = Tk()
    root.title("3D Object Repair kit")
    root.iconbitmap('')
    root.geometry("500x250")

    def convert():
        print("hey")

    Convert_btn = Button(root, text="Convert", command=convert)

    def open():
        global errorlbl
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select a .stl file",filetypes=(("stl files", "*.stl"), ("all files", "*.*")))
        errorlbl = Label(root, text="[ERROR] Not a valid file, please select a stl file")
        Convert_btn.pack()
        if(not checkFile(root.filename)):
            errorlbl.pack()
            Convert_btn["state"] = "disabled"

    upload_btn = Button(root, text="Open File", command=open())
    upload_btn.pack()

    root.mainloop()
