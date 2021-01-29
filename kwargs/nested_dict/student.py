f=open("student","r")

students={}
for lines in f:
    id,name,total,course=lines.rstrip("\n").split(",")

    if id not in students:
        students[id]={"id":id,"name":name,"total":total,"course":course}


def print_data(**kwargs):
    #print(kwargs)
    id=kwargs["id"]
    if id in students:
        print(students[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(students[id][prop])
    else:
        print("Student doesn't exist")

print_data(id="1002",prop="course")