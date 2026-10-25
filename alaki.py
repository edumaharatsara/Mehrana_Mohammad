import subprocess
subprocess.call("cls",shell=True)
from tkinter import *# type: ignore
from tkinter import messagebox
from tkinter import ttk
from random import *# type: ignore
import os

fooddic={"pizza":[320,1201,10],
         "burger":[400,1202,20],
         "salad":[100,1203,10],
         "Coca":[20,1204,30]}
new_item=input("Enter food Name For Edit : ")
if new_item in fooddic:
    oldvalues=fooddic[new_item]
    choice=int(input("1-Price 2-Code  3-Off 4-None :"))
    if choice==1:
        newprice=float(input("Enter New Price : "))
        newvalues=[newprice,oldvalues[1],oldvalues[2]]
    elif choice==2:
        newcode=float(input("Enter New Price : "))
        newvalues=[oldvalues[0],newcode,oldvalues[2]]
    elif choice==3:
        newoff=float(input("Enter New Price : "))
        newvalues=[oldvalues[0],oldvalues[1],newoff]
    else:
        newvalues=oldvalues
else:
    newvalues=[460,1003,20]  #  please Get all data for New Item 
fooddic[new_item]=newvalues
os.remove("food.txt")
fp=open("food.txt","w")
for key in fooddic:
    values=fooddic[key]
    foodname=key
    price=values[0]
    code=values[1]
    off=values[2]
    data=foodname+","+str(price)+","+str(code)+","+str(off)+",\n"
    fp.write(data)
fp.close()
fp=open("food.txt","r")
print(fp.read())


input("...")

