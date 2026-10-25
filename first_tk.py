import subprocess
subprocess.call("cls",shell=True)
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import *
show="off"   # public 

def Create_Captcha(lencaptcha):
    method=randint(1,4)
    cap=""
    for i in range(lencaptcha):
        if method==1:
            cap+=chr(randint(48,57))
        if method==2:
            cap+=chr(randint(65,90))
        if method==3:
            cap+=chr(randint(97,122))
        if method==4:
            choice=randint(1,3)
            if choice==1:
                cap+=chr(randint(48,57))
            if choice==2:
                cap+=chr(randint(65,90))
            if choice==3:
                cap+=chr(randint(97,122))  
    return cap


def Login_Page():
    # x=100  #  local
    # global show   #  global 
    def Goto_Roshan():
        p1.destroy()
        Roshan_Page()

    def Show_Hide_Password():
        global show
        if show=="off":
            show="on"
            e2.config(show="")
            b2.config(text="Hide")
        else:
            show="off"
            e2.config(show="•")
            b2.config(text="Show")

    def New_Captcha():
        e4.config(state="normal")
        cap=Create_Captcha(4)
        e4.delete(0,END)
        e4.insert(0,cap)
        e4.config(state="readonly")

    p1=Tk()
    p1.title("Login Page")
    p1.geometry("400x300")
    p1.config(bg="#A5F8AC")

    l1=Label(p1,text="User :")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)

    l2=Label(p1,text="Password :")
    l2.place(x=10,y=50)
    e2=Entry(p1,show="•")   #  win = .           alt+NumLock(7)
    e2.place(x=100,y=50)
    b2=Button(p1,text="Show",width=8,command=Show_Hide_Password)
    b2.place(x=230,y=50)

    l3=Label(p1,text="User Captcha:")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)
    e3.bind('<Control-c>',lambda e:'break')
    e3.bind('<Control-x>',lambda e:'break')
    e3.bind('<Control-v>',lambda e:'break')

    l4=Label(p1,text="Captcha:")
    l4.place(x=10,y=130)
    e4=Entry(p1,font=("Vivaldi",10))
    e4.place(x=100,y=130)
    cap=Create_Captcha(4)
    e4.insert(0,cap)
    e4.config(state="readonly")
    e4.bind('<Control-c>',lambda e:'break')
    e4.bind('<Control-x>',lambda e:'break')
    e4.bind('<Control-v>',lambda e:'break')
    b4=Button(p1,text="New Captcha",command=New_Captcha)
    b4.place(x=230,y=130)


    b1=Button(p1,text="Login",width=17,command=Goto_Roshan)
    b1.place(x=100,y=170)


    p1.mainloop()

def Roshan_Page():
    def Goto_Login():
        p1.destroy()
        Login_Page()

    p1=Tk()
    p1.title("Roshan Page")
    p1.geometry("700x400")
    p1.config(bg="#ED5CAC")

    b1=Button(p1,text="Logout",command=Goto_Login)
    b1.place(x=200,y=100)


    p1.mainloop()



Login_Page()
