import subprocess
subprocess.call("cls",shell=True)

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

data="="*60+"\n"
cnt=0
s1=0;s2=0;s3=0;s4=0
while True:
    gold=input("Enter Gold : ")
    if gold=="":
        break
    cnt+=1
    vazn=Get_Float("Enter Weight[ 0.1 - 500 ] :",0.1,500)
    gheimat=Get_Float("Enter Price : ",1000,100000)
    karmozd=Get_Int("Enter Profit : ",0,15)
    maliat=Get_Float("Enter Tax : ",0,100)
    p1=vazn * gheimat        ; s1+=p1
    p2=p1 * karmozd /100     ;s2+=p2
    p3=p1 * maliat /100      ;s3+=p3
    p4=p1 +p2 + p3           ;s4+=p4
    data+="{0:25s}{1:12.1f}{2:12.1f}{3:12.1f}{4:12.1f}{5:12.1f}{6:12.1f}".format(gold,vazn,gheimat,p1,p2,p3,p4)+"\n"
data+="="*60+"\n"
if cnt!=0:
    name=input("Enter name : ")
    mobile=Get_Int("Enter Mobile : ",9000000000,9999999999)
    print(name,mobile)
    print("="*60)
    print(data)
    print("="*60)
    print(s1,s2,s3, "          -->  Payment :",s4)





