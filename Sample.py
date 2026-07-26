import subprocess
subprocess.call("cls",shell=True)
Student_Name=input("Please Enter Student name:")
Code_Melli=int(input("Please Enter Code Melli:"))
Address=input("Please Enter Address:")
data="===================================================================\n"
data+="{0:30s}{1:15d}\t{2:50s}".format(Student_Name,Code_Melli,Address)+"\n"
tedad_dars=int(input("Please Enter tedad_dars:"))
for i in range(tedad_dars):
    Lesson_Name=input("Please Enter Lesson_Name:")
    Teacher_Name=input("Please Enter Teacher_Name:")
    Nomreh=float(input("Please Enter Nomreh:"))
    Zarib_Dars=int(input("Please Enter Zarib_Dars:"))
    data+="{0:2d}-{1:20s}{2:20s}{3:10.2f}{4:10d}".format(i+1,Lesson_Name,Teacher_Name,Nomreh,Zarib_Dars)+"\n"
data+="==================================================================\n"
print(data) 




