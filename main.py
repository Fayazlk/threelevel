from subprocess import Popen
from tkinter import *

from PIL import ImageTk, Image
import sqlite3
import os
root = Tk()
root.geometry('1366x768')
root.title("ThreeLevel")

def server():
     root.destroy()
     os.system('python adminlogin.py')




def client():
    root.destroy()
    os.system('python login.py')

def reg():

    #os.system("python register.py")
    Popen("python register.py")


def textlogin():
    Popen('python login.py')


def colorlogin():
    Popen('python color.py')
def imglogin():
    Popen('python img.py')

canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)

img1 = Image.open('admin.png')
photo1 = ImageTk.PhotoImage(img1)
img2 = Image.open('user.png')
photo2 = ImageTk.PhotoImage(img2)
img3 = Image.open('graph.png')
photo3 = ImageTk.PhotoImage(img3)
img4 = Image.open('reg.png')
photo4 = ImageTk.PhotoImage(img4)
Button(root,  image=photo1, width=200,height=200, bg='black', fg='white',font=("bold", 20) ,command=textlogin).place(x=900, y=100)

Button(root,  image=photo2, width=200, height=200,bg='black', fg='white', font=("bold", 20),command=colorlogin).place(x=1100, y=100)

Button(root,  image=photo3, width=200, height=200,bg='black', fg='white', font=("bold", 20),command=imglogin).place(x=900, y=300)

Button(root,  image=photo4, width=200, height=200,bg='black', fg='white', font=("bold", 20),command=reg).place(x=1100, y=300)

root.mainloop()
