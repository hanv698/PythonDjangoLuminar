num=int(input("Enter num:"))
flag=0
if(num==1):
    print("Neither prime nor composite")
else:
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
        else:
            flag=0
    if(flag==0):
        print(num,"is prime")
    else:
        print(num,"is not prime")