from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image, ImageTk, ImageFilter


#def login():
#    if usernameEntry.get()=='' or passwordEntry.get()=='':
#        messagebox.showerror('Error','Fields cannot be empty')
#    elif usernameEntry.get()=='mahmoud' and passwordEntry.get()=='1234':
#        messagebox.showinfo('Success','Welcome')
#
#    else:
#        messagebox.showerror('Error','Please enter correct credentials')

import subprocess

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='mahmoud' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Welcome')
        subprocess.run(['python', 'sms.py'])
    else:
        messagebox.showerror('Error','Please enter correct credentials')


window=Tk()

window.geometry('1280x700+0+0')

window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='grey', highlightthickness=5)
loginFrame.place(x=400,y=150)


logoImage=PhotoImage(file='logo.png')

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='grey')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='grey')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15
                   ,fg='cornflowerblue',bg='cornflowerblue',activebackground='white',
                   activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)



window.mainloop()
