import subprocess
subprocess.call("cls",shell=True)
from tkinter import *
from tkinter import ttk
studentdic={"Mahdi":9112921512,
            "Mohammad":9123212332,
            "Hadi":9133214567}
studentlist=[]
for item in studentdic:
    studentlist.append(item)

def Login_Page():

    def Load(*args):
        name=c1.get()
        mobile=studentdic[name]
        e1.delete(0,END)
        e1.insert(0,mobile)

    p1=Tk()
    p1.title("Login Page")
    p1.geometry("400x300")
    p1.config(bg="#F83A1D")
    l1=Label(p1)
    l1.config(text="User Name :")
    l1.place(x=10,y=10)

    e1=Entry(p1)
    e1.place(x=100,y=10)

    b1=Button(p1,text="Login",width=17)
    b1.place(x=100,y=40)

    c1=ttk.Combobox(p1)
    c1.place(x=250,y=40)
    c1["values"]=studentlist
    c1.bind("<<ComboboxSelected>>",Load)

    p1.mainloop()

Login_Page()
