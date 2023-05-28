from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import os
main=Tk()

total_height=main.winfo_screenheight()
total_width=main.winfo_screenwidth()

main.title("M.I.E.T. ENGINEERING COLLEGE STUDENT MANAGEMENT SYSTEM")
main.geometry(f"{int(total_width*0.7)}x{int(total_height*0.7)}")

windowwidth=main.winfo_width()
windowheight=main.winfo_height()

logo = ImageTk.PhotoImage(Image.open('mietlogo.png').resize((250,150)))

logoframe = Frame(main,background="cadetblue3")
logoframe.pack(side=LEFT, fill=BOTH,expand=True)

loginframe= Frame(main,background="cadetblue2",width=total_width*0.2)
loginframe.pack(side=RIGHT, fill=BOTH, expand=True)

logolabel=Label(logoframe,image=logo)
logolabel.place(relx=0.25,rely=0.4)

loginlogo=ImageTk.PhotoImage(Image.open("login1.png").resize((100,100)))

loginlogolabel=Label(loginframe,image=loginlogo,background="cadetblue2")
loginlogolabel.place(relx=0.5,rely=0.2,anchor=CENTER)

usernamelabel=Label(loginframe,text="Username :",background="cadetblue2",font=("Arial Rounded MT Bold",15))
usernamelabel.place(relx=0.36,rely=0.4,anchor=CENTER)

usernameentry=Entry(loginframe,border=2.5,font=('Arial Rounded MT',13))
usernameentry.place(relx=0.5,rely=0.45,anchor=CENTER,height=40,width=350)

passwordlabel=Label(loginframe,text="Password :",background="cadetblue2",font=("Arial Rounded MT Bold",15))
passwordlabel.place(relx=0.36,rely=0.54,anchor=CENTER)

passwordentry=Entry(loginframe,border=2.5,font=('Arial Rounded MT',13),show="•")
passwordentry.place(relx=0.5,rely=0.59,anchor=CENTER,height=40,width=350)

v = StringVar(loginframe, "staff")

student_radio_button=Radiobutton(loginframe,text="Student",font=("Arial Rounded MT Bold",15),variable=v,value="student",background="cadetblue2")
student_radio_button.place(relx=0.4,rely=0.7,anchor=CENTER)

staff_radio_button=Radiobutton(loginframe,text="Staff",font=("Arial Rounded MT Bold",15),variable=v,value="staff",background="cadetblue2")
staff_radio_button.place(relx=0.6,rely=0.7,anchor=CENTER)

def login():
    username=usernameentry.get()
    password=passwordentry.get()
    if username!="mietuser":
        messagebox.showwarning("Warning","Invalid Username/ID")
    elif password != "password":
        messagebox.showwarning("Warning","Invalid Password")
    else:
        if v.get()=="student":
            main.destroy()
            os.system("python Homepage.py")
        else:
            messagebox.showinfo("Information","Staff Module Under development")

login_button=Button(loginframe,text="Login",width=20,height=2,background="cadetblue3",command=login)
login_button.place(relx=0.5,rely=0.8,anchor=CENTER)

main.mainloop()