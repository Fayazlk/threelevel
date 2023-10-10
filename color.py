from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
import sqlite3
import os
root = Tk()
root.geometry('1366x768')
root.title("ThreeLevel")
x1=StringVar()
x2=StringVar()
x3=StringVar()
X=StringVar()
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
x2=StringVar()
x2=""
def clear():
    global x2
    x2=""
    X.set(x2)
def c1():
    global x2
    x1="R"
    x2=x2+x1
    X.set(x2)

def c2():
    global x2
    x1 = "Bl"
    x2 = x2 + x1
    X.set(x2)

def c3():
    global x2
    x1 = "G"
    x2 = x2 + x1
    X.set(x2)

def c4():
    global x2
    x1 = "Y"
    x2 = x2 + x1
    X.set(x2)

def c5():
    global x2
    x1 = "W"
    x2 = x2 + x1
    X.set(x2)

def c6():
    global x2
    x1 = "B"
    x2 = x2 + x1
    X.set(x2)
def auth():
    conn = sqlite3.connect('Form.db')
    dbuser = "-"
    dbpw = "-"

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM temp")
        rows = cur.fetchall()
        for row in rows:
            dbuser = row[0]
            dbpw = row[1]
        cur.execute("SELECT * FROM register where fullname=? and email=?",(dbuser,dbpw))
        rows = cur.fetchall()

        xxx2 = "-"
        for row in rows:
            xx1 = row[3]
            xx2 = row[4]
            xx3 = row[5]
            xxx2=xx1+xx2+xx3
        xxx1 = X.get()
        print(xxx1)
        print(xxx2)
        if xxx1==xxx2:

            messagebox.showinfo("Login", " Image Authentication is Successfull")
            root.destroy()
        else:
           messagebox.showinfo("Login", " Try Again")
l1=Label(root,text="Select Any three Colors", font=("bold", 20))
l1.place(x=900,y=200)
Button(root,   bg='red', font=("bold", 20) ,command=c1).place(x=900, y=300)

Button(root,  bg="blue",font=("bold", 20),command=c2).place(x=950, y=300)

Button(root,   bg="green", font=("bold", 20),command=c3).place(x=1000, y=300)

Button(root,  bg="yellow",font=("bold", 20),command=c4).place(x=900, y=400)
Button(root,  bg="white",font=("bold", 20),command=c5).place(x=950, y=400)
Button(root,  bg="black",font=("bold", 20),command=c6).place(x=1000, y=400)
Button(root,  text="Clear",font=("bold", 12),command=clear).place(x=1150, y=50)
Button(root,  text="Image Authentication",bg="black",fg="white",font=("bold", 12),command=auth).place(x=1000, y=600)
t1=Entry(root,textvar=X)
t1.place(x=1000,y=50)

root.mainloop()
