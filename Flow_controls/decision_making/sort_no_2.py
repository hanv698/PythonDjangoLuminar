num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("Sorted:",num1,num2,num3)
    else:
        temp=num2
        num2=num3
        num3=temp
        print("Sorted:",num1,num2,num3)
elif((num2>num3)&(num2>num1)):
    temp=num1
    num1=num2
    num2=temp
    if(num2>num3):
        print("Sorted:",num1,num2,num3)
    else:
        temp=num2
        num2=num3
        num3=temp
        print("Sorted:",num1,num2,num3)
elif((num3>num1)&(num3>num2)):
    temp=num1
    num1=num3
    num3=temp
    if(num2>num3):
        print("Sorted:",num1,num2,num3)
    else:
        temp=num2
        num2=num3
        num3=temp
        print("Sorted:",num1,num2,num3)