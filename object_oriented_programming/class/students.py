class Student:
    def __init__(self,roll,name,course,total):
        self.roll=roll
        self.name=name
        self.course=course
        self.total=total

    def __str__(self):
        return self.name


stud1=Student(1000,"Hanna","django",200)
stud2=Student(1001,"Haroon","mean",250)
stud3=Student(1002,"Hammam","django",300)

s_list=[]
s_list.append(stud1)
s_list.append(stud2)
s_list.append(stud3)

tot=0

for stud in s_list:
    #print(stud)
    if stud.course=="django":
        print(stud.name)
        tot += stud.total

print(tot)


