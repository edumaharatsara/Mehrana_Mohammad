import subprocess
subprocess.call("cls",shell=True)
from random import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

studentdic={"mani":[1234,"Python"],
            "shadlin":[3245,"AI"],
            "mohammadreza":[4352,"ML"]}

studentlist=[]
for key in studentdic:
    studentlist.append(key)

def Student_page():
    def Show_St_Info(*args):
        key=c1.get()
        values=studentdic[key]
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(0,key)
        e2.insert(0,values[0])
        e3.insert(0,values[1])
    p1=Tk()
    p1.title("Login Page")
    p1.geometry("700x500")
    p1.resizable(False,False)
    p1.config(bg="#20558B")

    l1=Label(p1,text="St Name :")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)

    l2=Label(p1,text="St Code")
    l2.place(x=10,y=50)
    e2=Entry(p1)
    e2.place(x=100,y=50)

    l3=Label(p1,text="Course")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)

    v1=StringVar()
    c1=ttk.Combobox(p1,textvariable=v1)
    c1.place(x=400,y=10)
    c1.set("Student Name")
    c1["values"]=studentlist
    c1.bind("<<ComboboxSelected>>",Show_St_Info)

    p1.mainloop()
Student_page()