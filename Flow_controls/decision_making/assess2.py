num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
num3=int(input("Enter num3:"))

if((num1>num2)&(num1>num3)):
    print("Num1 is highest")
elif(num2>num1)&(num2>num3):
    print("num2 is highest")
elif((num3>num1)&(num3>num2)):
    print("Num3 is highest")
else:
    print("All Equal")
