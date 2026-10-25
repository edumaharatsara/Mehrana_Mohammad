import subprocess
subprocess.call("cls",shell=True)
from tkinter import *# type: ignore
from tkinter import messagebox
from tkinter import ttk
from random import *# type: ignore
fooddic={}
foodlist=[]
fn="food.txt"
def Get_Data_From_File():
    global fooddic,foodlist
    fp=open(fn,"r")
    while True:
        x=fp.readline()
        if x=="":
            break
        y=x.split(",")
        foodname=y[0]
        price=float(y[1])
        code=int(y[2])
        off=float(y[3])
        fooddic[foodname]=[price,code,off]
        foodlist.append(foodname)
    fp.close()
Get_Data_From_File()

def Food_Page():
    def Show_Food_info(*args):
        key=c1.get()
        values=fooddic[key]
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e1.insert(0,key)
        e2.insert(0,values[0])
        e3.insert(0,values[1])
        e4.insert(0,values[2])

    def Factor():
        foodname=e1.get()
        if foodname not in fooddic:
            c1.focus()
            return
        price=float(e2.get())
        code=e3.get()
        off=float(e4.get())
        num=float(e5.get())

        hesab1=price * num 
        hesab2=hesab1 * off /100
        hesab3=hesab1 - hesab2
        data="{0:20s}{1:12.1f}{2:5.1f}{3:12.1f}$-{4:12.1f}={5:12.1f}Pay".format(foodname,price,num,hesab1,hesab2,hesab3)+"\n"
        q=messagebox.askyesno("Confirm",data)
        if q==True:
            t1.insert(END,data)
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)

    def Add_item():
        pass
    p1=Tk()
    p1.title("Login Page")
    p1.geometry("900x700")
    p1.config(bg="#20A3B2")

    l1=Label(p1,text="Food Name :")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)

    l2=Label(p1,text="Price :")
    l2.place(x=10,y=50)
    e2=Entry(p1) 
    e2.place(x=100,y=50)

    l3=Label(p1,text="Code :")
    l3.place(x=10,y=90)
    e3=Entry(p1)
    e3.place(x=100,y=90)


    l4=Label(p1,text="Off :")
    l4.place(x=10,y=130)
    e4=Entry(p1) 
    e4.place(x=100,y=130)

    l5=Label(p1,text="Num :")
    l5.place(x=10,y=170)
    e5=Entry(p1) 
    e5.place(x=100,y=170)
    e5.insert(0,1)
    
    b1=Button(p1,text="Factor",width=17,command=Factor)
    b1.place(x=400,y=50)

    t1=Text(p1,width=120,height=20)
    t1.place(x=10,y=200)


    v1=StringVar()
    c1=ttk.Combobox(p1,textvariable=v1)
    c1.place(x=400,y=10)
    c1.set("Food Name")
    c1["values"]=foodlist
    c1.bind("<<ComboboxSelected>>",Show_Food_info)

    b2=Button(p1,text="Add Item",width=17,command=Add_Item)
    b2.place(x=400,y=90)



    p1.mainloop()
Food_Page()




