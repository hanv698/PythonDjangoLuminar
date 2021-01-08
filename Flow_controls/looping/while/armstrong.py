num=int(input("Enter the no:"))
num1=num
res=0
while(num>0):
    digit=num%10
    res=res+(digit**3)
    num = num//10
print("Result of",num1,":",res)