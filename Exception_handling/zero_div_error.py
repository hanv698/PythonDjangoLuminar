num1=int(input())
num2=int(input())

try:
    res=num1/num2
    print("Result:",res)
except Exception as e:
    print("ZeroDivisionError")

print("Program completed")