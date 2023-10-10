from tkinter import *
import sqlite3
import os
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
root = Tk()
root.geometry('1366x768')
root.title("Login")
canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
Faceimg = StringVar()
Un = StringVar()
Pw = StringVar()
Faceimg = StringVar()
def back():
    root.destroy()
    os.system('python main.py')

def login():
    un = Un.get()
    pw = Pw.get()
    l=len(pw)
    faceimg= Faceimg.get()
    if un=="":
        messagebox.showinfo("Pw","Enter Username")
    else:
        if pw == "":
            messagebox.showinfo("Pw","Enter Password")
        else:
            if l!=11:
                messagebox.showinfo("Pw", "Enter 11 character password")
            else:
                        print("aaa") 
                        dbuser = "-"
                        dbpw= "-"
                        conn = sqlite3.connect('Form.db') 
                        with conn:
                            cur = conn.cursor()
                            cur.execute("SELECT * FROM register  ")
                            rows = cur.fetchall()
                            for row in rows:
                                dbuser = row[1]
                                dbpw=row[6]
                                name1=row[0]
                                email=row[1]
                                
                            if dbuser!=un:
                                    messagebox.showinfo("Login", " Invalid Username")
                            else:
                                    if dbpw!=pw:
                                        messagebox.showinfo("Login", " Invalid Password")
                                    else:
                                         if dbuser == un and dbpw == pw :
                                            messagebox.showinfo("Login", " Textual Authentication is Successfull")
                                            conn = sqlite3.connect('Form.db')
                                            with conn:
                                                cur = conn.cursor()
                                                cur.execute("delete from temp")
                                                cur.execute( 'INSERT INTO temp (fname,Email) VALUES(?,?)', (name1, email))
                                                root.destroy()    



                         
                    


                    
                        



label_0 = Label(root, text="Text Authentication", bg='white', width=20, font=("bold", 20))
label_0.place(x=900, y=250)
label_1 = Label(root, text="E-Mail", width=20, bg='white', font=("bold", 10))
label_1.place(x=900, y=350)
entry_2 = Entry(root, textvar=Un)
entry_2.place(x=1100, y=350)
label_3 = Label(root, text="Password", width=20,bg='white', font=("bold", 10))
label_3.place(x=900, y=400)
entry_6 = Entry(root, textvar=Pw, show="*")
entry_6.place(x=1100, y=400)



Button(root, text='Login', width=20, bg='gray', fg='white', command=login).place(x=900, y=550)
Button(root, text='Cancel', width=20, bg='gray', fg='white', command=back).place(x=1050, y=550)


root.mainloop()


