import subprocess
subprocess.call("cls",shell=True)
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from module import *
import os

def File_Editting():
    def Create_File():
        fn=e1.get()
        fn=Set_FileName(fn)
        if fn==-1:
            e1.delete(0,END)
            e1.focus()
            return
        if os.path.exists(fn):
            msg=fn+"  Does Exist (Recreate It ?) :"
            q=messagebox.askyesno("Confirm",msg)
            if q==True:
                fp=open(fn,"w")
                fp.close()
        else:
            fp=open(fn,"x")
            fp.close()

    def Rename_File():
        fn1=e1.get()
        fn1=Set_FileName(fn1)
        if fn1==-1:
            e1.delete(0,END)
            e1.focus()
            return

        fn2=e2.get()
        fn2=Set_FileName(fn2)
        if fn2==-1:
            e2.delete(0,END)
            e2.focus()
            return

        if os.path.exists(fn1)==False:
            msg=fn1+"  Does Not Exist"
            messagebox.showwarning("Error",msg)
            e1.focus()
            return
        if os.path.exists(fn2):
            msg=fn2+"  Does Exist and Should be Removed!!! ? "
            q=messagebox.askyesno("Error",msg)
            if q==False:
                e2.delete(0,END)
                e2.focus()
                return
        os.remove(fn2)
        os.rename(fn1,fn2)
        
    def Delete_File():
        fn1=e1.get()
        fn1=Set_FileName(fn1)
        if fn1==-1:
            e1.delete(0,END)
            e1.focus()
            return

        if os.path.exists(fn1)==False:
            msg=fn1+"  Does Not Exist For Delete !!!!"
            messagebox.showwarning("Error",msg)
            e1.focus()
            return

        if os.path.exists(fn1):
            msg=fn1+"  Does Exist and Should be Removed!!! ? "
            q=messagebox.askyesno("Error",msg)
            if q==True:
                # Another Confirm !!!  2
                os.remove(fn1)
                e1.delete(0,END)
                e1.focus()

    p1=Tk()
    p1.title("File Handler")
    p1.geometry("600x400")
    p1.config(bg="#20A3B2")

    l1=Label(p1,text="File1 Name1 :")
    l1.place(x=10,y=10)
    e1=Entry(p1)
    e1.place(x=100,y=10)

    l2=Label(p1,text="File Name2 :")
    l2.place(x=10,y=50)
    e2=Entry(p1) 
    e2.place(x=100,y=50)
    
    b1=Button(p1,text="Create_File",width=17,command=Create_File)
    b1.place(x=300,y=10)

    b2=Button(p1,text="Rename_File",width=17,command=Rename_File)
    b2.place(x=300,y=50)

    b3=Button(p1,text="Delete_File",width=17,command=Delete_File)
    b3.place(x=300,y=90)


    p1.mainloop()
File_Editting()