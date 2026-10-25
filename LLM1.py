import subprocess
subprocess.call("cls",shell=True)
from tkinter import * 
from tkinter import messagebox
text1="My name is Hadi and my Expert is AI and\n" \
" Machine Learning . اما هوش مصنوعی با یادگیری ماشین متفاوت است \n" \
" . and AI can help up for Learning Machine . \n" \
"Other wise we can use ML and DL for Runnug and AI Project . "
text2="graphic design is very nice method for earning money .\n" \
"Todays some people are runnig grapgic method for earning money\n " \
". nut I am disagree with graphic design \n"
text3="Trade is very hard method for earnig money.\n" \
"I like earning money by trade .\n " \
"you can use AI for Earning Money.\n"


def Chat():
    t1.delete("1.0",END)
    q=e1.get()
    if q=="":
        return
    cnt=0
    found=False
    if text1.upper().find(q.upper())>=0:
        cnt+=1
        res1=str(cnt)+"-"+text1
        t1.insert(END,res1)
        found=True
    if text2.upper().find(q.upper())>=0:
        cnt+=1
        res2="\n"+str(cnt)+"-"+text2
        t1.insert(END,res2)
        found=True
    if text3.upper().find(q.upper())>=0:
        cnt+=1
        res3="\n"+str(cnt)+"-"+text3
        t1.insert(END,res3)
        found=True
    if found==False:
        t1.insert(END,"مطلبی با این عنوان یافت ")
    e1.delete(0,END)

hadi=Tk()
hadi.geometry("600x400")
hadi.title("LLM  Model ")

e1=Entry(hadi)
e1.place(x=10,y=10)

b1=Button(hadi,text="Chat",command=Chat)
b1.place(x=150,y=10)

t1=Text(hadi,width=140,height=30)
t1.place(x=10,y=40)


hadi.mainloop()



