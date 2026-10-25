import subprocess
subprocess.call("cls",shell=True)
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import *
show="off"   # public 
userdic={"hadi":["111","admin"],
         "mohammad":["222","user"],
         "mahdi":["333","operator"],
         "shamila":["444","admin"],
         "ali":["555","user"],
         }

name="roshan" ; passw="666" ;   kind2="operator"
userdic[name]=[passw,kind2]

username=""
userpassword=""
usertype=""

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
    def Sign_In():
        user=e1.get()
        if user not in userdic:
            messagebox.showwarning("Error","User ID False")
            e1.focus()
            return
        values=userdic[user]  # "hadi"
        password=values[0]    #"111"
        kind=values[1]      #"admin"

        entrypassword=e2.get()
        if entrypassword!=password:
            messagebox.showwarning("Error","Password False")
            e2.focus()
            return

        mycap=e3.get()
        syscap=e4.get()
        if mycap.upper()!=syscap.upper():
            messagebox.showwarning("Error","Security Code False")
            New_Captcha()
            e3.delete(0,END)
            e3.focus()
            return
        global username,userpassword,usertype
        username=user
        userpassword=password
        usertype=kind
        
        
        p1.destroy()
        My_Store_page()

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

    def Sign_In_Admin():
        user=e1.get()
        if user not in userdic:
            messagebox.showwarning("Error","User ID False")
            e1.focus()
            return
        values=userdic[user]  # "hadi"
        password=values[0]    #"111"
        kind=values[1]      #"admin"
        if kind!="admin":
            messagebox.showwarning("Sorry","You can not login to this section !!!")
            e1.focus()
            return

        entrypassword=e2.get()
        if entrypassword!=password:
            messagebox.showwarning("Error","Password False")
            e2.focus()
            return

        mycap=e3.get()
        syscap=e4.get()
        if mycap.upper()!=syscap.upper():
            messagebox.showwarning("Error","Security Code False")
            New_Captcha()
            e3.delete(0,END)
            e3.focus()
            return
        global username,userpassword,usertype
        username=user
        userpassword=password
        usertype=kind
        
        
        p1.destroy()
        Admin_page()



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
    e4=Entry(p1)     #   ,font=("Vivaldi",10))
    e4.place(x=100,y=130)
    cap=Create_Captcha(4)
    e4.insert(0,cap)
    e4.config(state="readonly")
    e4.bind('<Control-c>',lambda e:'break')
    e4.bind('<Control-x>',lambda e:'break')
    e4.bind('<Control-v>',lambda e:'break')
    b4=Button(p1,text="New Captcha",command=New_Captcha)
    b4.place(x=230,y=130)


    b1=Button(p1,text="Login",width=17,command=Sign_In)
    b1.place(x=100,y=170)

    b5=Button(p1,text="Goto Admin",width=17,command=Sign_In_Admin)
    b5.place(x=100,y=200)

    p1.mainloop()

def My_Store_page():
    def Log_Out():
        p1.destroy()
        Login_Page()

    p1=Tk()
    p1.title("Roshan Page")
    p1.geometry("900x600")
    p1.config(bg="#31FB37")

    b1=Button(p1,text="Logout",command=Log_Out)
    b1.place(x=200,y=100)

    b2=Button(p1,text="Change pass")
    b2.place(x=200,y=150)

    b3=Button(p1,text="Delete Accout")
    b3.place(x=200,y=200)

    if usertype=="user":
        b3.config(state="disabled")
    if usertype=="operator":
        b2.config(state="disabled")
        b3.config(state="disabled")
    


    p1.mainloop()



def Admin_page():
    def Log_Out():
        p1.destroy()
        Login_Page()
    def Confirm():
        user=c1.get()
        key=c2.get()
        if key=="Operator":
            c2.focus()
            return
        if key=="Delete":
            e1.place(x=380,y=40)
            if user not in userdic:
                c1.focus()
                return
            word=e1.get()
            if word!="CONFIRM":
                messagebox.showwarning("Alarm","Please Type CONFIRM in Entery 1 ")
                e1.focus()
                return
            q=messagebox.askyesno("Delete User!","Are You Sure ! ")
            if q==True:
                x=10

    p1=Tk()
    p1.title("Roshan Page")
    p1.geometry("700x400")
    p1.config(bg="#CDF93D")

    v1=StringVar()
    c1=ttk.Combobox(p1,textvariable=v1)
    c1.place(x=10,y=10)
    users=[]
    for item in userdic:
        values=userdic[item]
        if values[1]!="admin":
            users.append(item)
    c1["values"]=users
    c1.set("User Names ")
    c1.config(state="readonly")





    v2=StringVar()
    c2=ttk.Combobox(p1,textvariable=v2)
    c2.place(x=200,y=10)
    c2["values"]=["Change ID","Change password","Upgrade","Delete"]
    c2.set("Operator")
    c2.config(state="readonly")

    b2=Button(p1,width=16,text="Confirm",command=Confirm)
    b2.place(x=380,y=10)    

    e1=Entry(p1)
    # e1.place(x=380,y=40)






    b1=Button(p1,text="Logout",command=Log_Out)
    b1.place(x=600,y=10)    


    p1.mainloop()



Admin_page()
# Login_Page()
