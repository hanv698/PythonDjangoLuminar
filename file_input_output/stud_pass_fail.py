f1=open("student","r")
f2=open("fail","r")

stud=set(f1)
fail=set(f2)

pas=stud.difference(fail)
print("Passed:",pas)





