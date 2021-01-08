#Reverse of a number

num=int(input("Enter the no:"))
num1=num
rev=0 #rev=""
while(num>0):
    digit=num%10
    rev=(rev*10)+digit#print(digit,end="") #rev=rev+str(digit)
    num = num//10
print("Reverse of ",num1,":",rev)
