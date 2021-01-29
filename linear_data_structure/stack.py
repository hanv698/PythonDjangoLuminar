stk=[]
size=int(input("Enter size of stack"))

top=-1
n=1

def push():
    print("Push operation of stack")
    global top
    top+=1
    element=int(input("Enter element:"))

    if(top<size):
        stk.insert(top,element)
    else:
        print("Stack overflow")
        top-=1
        print(top)

    print("--------------")

def pop():
    print("Pop operation of stack:")
    global top
    #top-=1
    if(top<0):
        print("Stack underflow")

    else:
        print(stk[top],"Element popped")
        top -= 1
        #print(top)
    print("-------------")

def display():
    print(stk)

while(n!=0):
    choice=int(input("Enter choice\n 1.Push\n 2.Pop\n 3.Display\n"))
    if(choice==1):
        push()
    elif(choice==2):
        pop()
    elif(choice==3):
        display()
    else:
        print("Invalid Option")

    n=int(input("Do you want to continue [press 0 to exit]"))





