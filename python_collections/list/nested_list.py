students=[
    [10,"ajay","bca",250],
    [11,"vjay","bca",240],
    [12,"sibin","bca",220],
    [13,"dino","mca",220],
    [14,"tom","mca",180],
    [15,"jain","mca",250],
]

#print name of students
for stud in students:
        print(stud[1])

print("-------")

#print students name with mark >240
for stud in students:
    if(stud[3]>240):
        print(stud[1])

print("-------")

#print sum total of marks
total=0
for stud in students:
    total+=stud[3]
print("Sum total:",total)

print("--------")

#calculate total of bca and mca
b_total=0
m_total=0

for stud in students:
    if(stud[2]=='bca'):
        b_total+=stud[3]
    else:
        m_total+=stud[3]

print("B_total:",b_total)
print("M_total:",m_total)

print("---------")


