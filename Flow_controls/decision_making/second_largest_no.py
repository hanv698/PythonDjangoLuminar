num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("Num2 is second highest")
    else:
        print("Num3 is second highest")
elif((num2>num3)&(num2>num1)):
    if(num1>num3):
        print("num1 is second highest")
    else:
        print("num3 is second highest")
else:
    if(num2>num1):
        print("Num2 is second highest")
    else:
        print("Num1 is second highest")