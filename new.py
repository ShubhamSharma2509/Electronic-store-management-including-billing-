from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('800x400+340+150')
        self.root.title("Electronic Store Management")
        self.root.config(bg="white")
        self.root.focus_force()

if __name__=="__main__":
    root=Tk()
    OBJ=categoryClass(root)
    root.mainloop()