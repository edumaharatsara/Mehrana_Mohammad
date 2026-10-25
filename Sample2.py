import subprocess
subprocess.call("cls",shell=True)
customer_name=input("Enter Customer name :")
code_posti=int(input("Enter Code Posti : "))
addres=input("Enter Address : ")
data="==============================================================\n"
data+="{0:20s}{1:15d}\t{2:30s}".format(customer_name,code_posti,addres)+"\n"
s1=0 ; s2=0 ; s3=0
while True:
    kala=input("Enter Kala : ")
    if kala=="":
        break
    gheimat=float(input("Enter Gheimat : "))
    tedad=int(input("Enter tedad :"))
    takhfif=float(input("Enter Takhfif % : "))
    hesab1=gheimat*tedad                     ; s1+=hesab1
    hesab2=hesab1* takhfif / 100             ; s2+=hesab2
    hesab3=hesab1 - hesab2                   ; s3+=hesab3
    data+="{0:20s}{1:12.2f}{2:6d}{3:12.2f}{4:12.2f}{5:12.2f}".format(kala,gheimat,tedad,hesab1,hesab2,hesab3)+"\n"
data+="==============================================================\n"
data+="{0:12.2f}$     -    {1:12.2f}%        ==>   {2:12.2f}$".format(s1,s2,s3)+"\n"
data+="==============================================================\n"
print(data)

