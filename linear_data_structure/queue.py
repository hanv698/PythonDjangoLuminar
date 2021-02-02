que=[]
size=int(input("Enter size of queue"))

front,rear=-1,-1
n=1

def insert():
    print("Insertion operation of queue")
    global rear,front
    rear+=1
    element=int(input("Enter element:"))

    if(rear<size):
        que.insert(rear,element)
    else:
        print("Queue full")
        rear-=1
        print("rear:",rear)
    front=0
    print("--------------")

def delete():
    print("Deletion operation of queue:")
    global front

    if(front>rear):
        print("Queue empty")

    else:
        print(que[front],"Element deleted")
        front+=1
        #print(top)
    print("-------------")

def display():
    print(que)

while(n!=0):
    choice=int(input("Enter choice\n 1.Insert\n 2.Delete\n 3.Display\n"))
    if(choice==1):
        insert()
    elif(choice==2):
        delete()
    elif(choice==3):
        display()
    else:
        print("Invalid Option")

    n=int(input("Do you want to continue [press 0 to exit]"))
