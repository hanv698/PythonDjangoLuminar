num=int(input("Enter num(1-9):"))
i=1
sum=0
j=0

if((num>=1) & (num<=9)):
    while(i<=num):
        j=(j*10)+num
        sum=sum+j
        i+=1
        flag=0
    print(sum)
else:
    print("INVALID")