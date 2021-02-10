class Employee:
    def __init__(self,eid,ename,desig,exp,salary):
        self.eid=eid
        self.ename=ename
        self.desig=desig
        self.exp=exp
        self.salary=salary

    def __str__(self):
        return self.ename

f=open("employees","r")
emp=[]

for lines in f:
    print(lines)
    eid,ename,desig,exp,salary=lines.rstrip("\n").split(",")
    emp.append(Employee(eid,ename,desig,exp,salary))

for employee in emp:
    if employee.desig=="developer":
        print(employee.ename)

sal_list=[]
for employee in emp:
    sal_list.append(employee.salary)
print("High salary:",max(sal_list))

print("=============================")

deve=list(filter(lambda em:em.desig == "developer",emp))
for emplo in deve:
    print(emplo)

#count=len(list(filter(lambda em:em.desig == "developer",emp)))
count=len(deve)
print(count)

high=max(list(map(lambda e:e.salary,emp)))
print(high)