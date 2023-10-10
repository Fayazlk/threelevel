from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

import os
from PIL import ImageTk, Image

root = Tk()
root.geometry('1366x768')
root.title("Registration Form")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1, 1, anchor=NW, image=photo)
Fullname = StringVar()
Email = StringVar()
Contact = StringVar()
C1 = StringVar()
C2 = StringVar()
C3 = StringVar()
Un = StringVar()
Pw = StringVar()
Age = StringVar()
Gkey = StringVar()
Faceimg = StringVar()


def cancel():
    root.destroy()
    os.system('python Main.py')


def database():
    name1 = Fullname.get()
    email = Email.get()
    contact = Contact.get()

    l = len(contact)

    c1 = C1.get()
    pw = Pw.get()
    c2 = C2.get()

    faceimg = Faceimg.get()
    c3 = C3.get()

    if name1 == "":
        messagebox.showinfo("ThreeLevel", "Enter Name")
    else:
        if email == "":
            messagebox.showinfo("ThreeLevel", "Enter Email")
        else:
            if contact == "":
                messagebox.showinfo("ThreeLevel", "Enter Contact")
            else:
                if C1 == "":
                    messagebox.showinfo("ThreeLevel", "Enter Color1")
                else:
                    if C2== "":
                        messagebox.showinfo("ThreeLevel", "Enter Color2")
                    else:
                        if C3 == "":
                            messagebox.showinfo("ThreeLevel", "Enter Color3")
                        else:
                         if pw == "":
                            messagebox.showinfo("ThreeLevel", "Enter Password")
                         else:
                            if not (re.search(regex, email)):
                                messagebox.showinfo("ThreeLevel", "Enter valid Email")
                            else:
                                if l != 10:
                                    messagebox.showinfo("ThreeLevel", "Enter 10 digits only")
                                else:
                                    if not name1.isalpha():
                                        messagebox.showinfo("ThreeLevel", "Enter Name in alphabets Only ")
                                    else:

                                            dbuser="-"
                                            ph1="-"
                                            conn = sqlite3.connect('Form.db')
                                            with conn:
                                                cursor = conn.cursor()
                                                cursor.execute("SELECT * FROM register")
                                                rows = cursor.fetchall()
                                                for row in rows:
                                                    dbuser = row[0]

                                                    ph1 = row[1]
                                                if dbuser == name1 and email == ph1:
                                                    messagebox.showinfo("Pw", "Already Registered")
                                                else:
                                                    cursor.execute(
                                                        'CREATE TABLE IF NOT EXISTS register (Fullname TEXT,Email TEXT,Contact TEXT,C1 TEXT,C3 TEXT,Pw TEXT,Faceimg TEXT)')
                                                    cursor.execute(
                                                        'INSERT INTO register (FullName,Email,Contact,c1,c2,c3,pw,Faceimg) VALUES(?,?,?,?,?,?,?,?)',
                                                        (name1, email, contact,c1,c2,c3,pw, faceimg,))

                                                    conn.commit()
                                                    messagebox.showinfo("Pw", "Record Saved")


def open_File():
    faceimg = askopenfilename(filetypes=[(".png", "*.png")])
    Faceimg.set(faceimg)
    fm = Faceimg.get()
    load = Image.open(fm)
    render = ImageTk.PhotoImage(load)

    # labels can be text or images
    img = Label(root, image=render)
    img.image = render
    img.place(x=600, y=100)


label_0 = Label(root, justify=LEFT, bg='white', text="Registration Here..", width=30, font=("bold", 20))
label_0.place(x=900, y=100)

label_1 = Label(root, text="FullName", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_1.place(x=900, y=200)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=1150, y=200)

label_2 = Label(root, text="Email", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_2.place(x=900, y=250)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=1150, y=250)

label_3 = Label(root, text="Contact", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_3.place(x=900, y=300)

entry_3 = Entry(root, textvar=Contact)
entry_3.place(x=1150, y=300)

label_4 = Label(root, text="Color 1", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_4.place(x=900, y=350)

entry_5 = Entry(root, textvar=C1)
entry_5.place(x=1150, y=350)

label_5 = Label(root, text="Color 2", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_5.place(x=900, y=400)

entry_6 = Entry(root, textvar=C2)
entry_6.place(x=1150, y=400)

label_7 = Label(root, text="Color 3", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_7.place(x=900, y=450)

entry_7 = Entry(root, textvar=C3)
entry_7.place(x=1150, y=450)

label_8 = Label(root, text="Password", bg='white', justify=LEFT, width=20, font=("bold", 10))
label_8.place(x=900, y=500)

entry_8 = Entry(root, textvar=Pw)
entry_8.place(x=1150, y=500)



entry_7 = Entry(root, textvar=Faceimg)
entry_7.place(x=700, y=200)

Button(root, text='Submit', width=10, bg='gray', fg='white', command=database).place(x=850, y=600)
Button(root, text='Cancel', width=10, bg='gray', fg='white', command=cancel).place(x=930, y=600)
Button(root, text='Browse Image', width=20, bg='gray', fg='white', command=open_File).place(x=1100, y=600)


root.mainloop()
