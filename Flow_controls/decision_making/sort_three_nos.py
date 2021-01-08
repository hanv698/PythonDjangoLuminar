num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("Sorted:",num1,num2,num3)
    else:
        print("Sorted:",num1,num3,num2)
elif((num2>num3)&(num2>num1)):
    if(num1>num3):
        print("Sorted:",num2,num1,num3)
    else:
        print("Sorted:",num2,num3,num1)
else:
    if(num2>num1):
        print("Sorted:",num3,num2,num1)
    else:
        print("Sorted:",num3,num1,num2)