def Get_Int(msg,range1,range2):
    while True:
        try:
            data=int(input(msg))
            if data>=range1 and data<=range2:
                break
            else:
                print("Range ",range1," To ",range2)
        except:
            print("Havaset Kojast ...")
    return data

def Get_Float(msg,range1,range2):
    while True:
        try:
            data=float(input(msg))
            if data>=range1 and data<=range2:
                break
            else:
                print("Range ",range1," To ",range2)
        except:
            print("Havaset Kojast ...")
    return data


def Get_Personal_Name(msg):
    while True:
        s=input(msg)
        s=str(s)
        if len(s)<3 : 
            print("Len >=3 !!!!")
            continue
        if s.count("  ")>0:
            print("Space Error !!!!")
            continue
        if s[0]==" ":             #    or s[len(s)]==" "
            print("First Char a-z A-Z !!!!")
            continue
        karam=True
        for i in s  : 
            if not(i==" " or i>="a" and i<="z" or  i>="A" and i<="Z"):
                karam=False
        if karam==False:
            print("Invalid Char  a-z  A-Z  space ...")
            continue
        break
    return s

def Get_lesson_Name(msg):
    while True:
        s=input(msg)
        s=str(s)
        karam=True
        for i in range(len(s)):
            if s[i]==" " and s[i+1]!="(":
                karam=False
        if karam==False:
            print("(  Error ")
            continue

        
        if (s[len(s)]-1)!=")":
            print(")  Error")
            continue





def Set_Float(n,r1,r2):
    try:
        n=float(n)
        if n>=r1 and n<=r2:
            return n
        else:
            return -1
    except:
        return -1

def Set_Int(n,r1,r2):
    try:
        n=int(n)
        if n>=r1 and n<=r2:
            return n
        else:
            return -1
    except:
        return -1



def Set_FileName(s):
    s=str(s)
    loc=s.find(".")
    if loc==0  or loc==len(s)-1 or s.count(".")==0 or s.count(".")>1:
        return -1
    if len(s)<4:
        return -1
    if s.count("/")+s.count("\\")+s.count("*")+s.count(":")!=0:
        return -1
    return s
    