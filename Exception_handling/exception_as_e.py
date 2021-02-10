num1=int(input("num1:"))
num2=int(input("num2:"))
pos=int(input("Position:"))

lst=[10,20,30]

try:
    res=num1/num2
    print("Result:", res)
    print(lst[pos])
except Exception as e:
    print(e.args)