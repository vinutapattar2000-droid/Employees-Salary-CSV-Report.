import csv
with open("emp.csv","w")as f:
    w=csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("Enter Number of Employess:"))
    for i in range(n):
      eno=input("Enter Employee No:")
      ename=input("Enter Employess Name:")
      esal=input("Enter Employee Salary:")                
      eaddr=input("Enter Employee Address:")
      w.writerow([eno,ename,esal,eaddr])
print("Total Employees data written to csv file successfully")
f=open("emp.csv",'r')
r=csv.reader(f)
data=list(r)
for line in data:
    for word in line:
        print(word,"\t",end="")
    print()