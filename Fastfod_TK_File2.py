import subprocess
subprocess.call("cls",shell=True)
from tkinter import *# type: ignore
from tkinter import messagebox
from tkinter import ttk
from module import *
from random import *# type: ignore
fooddic={}
foodlist=[]
fn="food.txt"
def Get_Data_From_File():
    global fooddic,foodlist
    fooddic={}
    foodlist=[]    
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

    def Add_Item():
        foodname=e1.get()
        if foodname=="":
            e1.focus()
            return 
        if foodname in fooddic:
            q=messagebox.askyesno("Message","Foodname does Exist in Menu !!!")
            if q==True:
                r=randint(10,99)
                foodname+=str(r)
                #####
            else:
                e1.delete(0,END)
                e1.focus()
                return
        price=e2.get()
        price=Set_Float(price,10,3000)
        if price==-1:
            e2.delete(0,END)
            e2.focus()
            return

        code=e3.get()
        code=Set_Int(code,1000,9999)
        if code==-1:
            e3.delete(0,END)
            e3.focus()
            return


        off=e4.get()
        off=Set_Float(off,0,100)
        if off==-1:
            e4.delete(0,END)
            e4.focus()
            return
        fp=open("food.txt","a")
        data=foodname+","+str(price)+","+str(code)+","+str(off)+",\n"
        fp.write(data)
        fp.close()
        Get_Data_From_File()
        c1["values"]=foodlist
        messagebox.showinfo("Ok","New Food has been added to Menu")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        c1.focus()

    def Search_Food():
        key=e6.get()
        if key=="":
            e6.focus()
            return
        found=False
        for i in fooddic:
            item=str(i)
            values=fooddic[i]
            if item.upper().find(key.upper())>=0:
                found=True
                foodname=item
                price=values[0]
                code=values[1]
                off=values[2]
                msg=foodname+"\t"+str(price)+"\t"+str(code)+"\t"+str(off)+"\t"
                q=messagebox.askyesno("Confirm",msg)
                if q==True:
                    e1.delete(0,END)
                    e1.insert(0,foodname)

                    e2.delete(0,END)
                    e2.insert(0,price)

                    e3.delete(0,END)
                    e3.insert(0,code)

                    e4.delete(0,END)
                    e4.insert(0,off)
                    break
        if found==False:
            messagebox.showinfo("Sorry","This Food Not Found !")

                


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


    l6=Label(p1,text="Search:")
    l6.place(x=350,y=130)
    e6=Entry(p1) 
    e6.place(x=400,y=130)
    b3=Button(p1,text="Search",width=17,command=Search_Food)
    b3.place(x=400,y=160)



    p1.mainloop()
Food_Page()




