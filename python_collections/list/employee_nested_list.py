employees=[
    [10,"christy","dataanalyst",50000],
    [11,"jhon","ba",30000],
    [12,"sab","dataanalyst",40000],
    [13,"tom","developer",40000],
    [14,"jhoni","developer",30000],
    [15,"sabir","dataanalyst",50000],
    [16,"tino","developer",40000],
    [17,"tomis","developer",47000],
    [18,"jhonis","developer",32000],

]

#print no of employees
len_emp=len(employees)
print("No of employees:",len_emp)

print("=============")

#print amount company need to rais ein month end
total_sal=0
for emp in employees:
    total_sal+=emp[3]
print("Total Salary:",total_sal)

print("=============")

#groupby designation wise
dev_cnt=0
da_cnt=0
ba_cnt=0
for emp in employees:
    if(emp[2]=='dataanalyst'):
        da_cnt+=1
    elif(emp[2]=='developer'):
        dev_cnt+=1
    else:
        ba_cnt+=1
print("No of developers:",dev_cnt)
print("No of data analyst:",da_cnt)
print("No of buisness analyst:",ba_cnt)

print("=============")

#print highest salaried emp name
sal_list=[]
for emp in employees:
    sal_list.append(emp[3])
high=max(sal_list)
print("Highest salary :",high)

print("***********")

print("Employees with highest salary:")
for emp in employees:
    if(emp[3]==high):
        print(emp[1])


print("=============")

#print lowest salary in developer name
dev_sal_list=[]

for emp in employees:
    if(emp[2]=='developer'):
        dev_sal_list.append(emp[3])
low=min(dev_sal_list)
print(dev_sal_list)

print("Lowest salary :",low)

print("***********")

print("Employees with lowest salary in developer:")
for emp in employees:
    if(emp[2]=='developer' and emp[3]==low):
        print(emp[1])
