#to print pass student name
students=["ajay","vijay","siraj","sooraj","ajay","akash","vijay","amal"]
fail=["ajay","amal"]

stud_set=set(students)
fail_set=set(fail)

pass_set=stud_set.difference(fail_set)
pas=list(pass_set)

print("Set:",pass_set)
print("List:",pas)