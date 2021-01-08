low_lim=int(input("Enter lower limit:"))
up_lim=int(input("Enter upper limit:"))
#num=int(input("Enter num:"))

for num in range(low_lim,(up_lim+1)):
    flag = 0
    for i in range(2,num):
        if(num%i==0):
            flag=1
            break
        else:
            flag=0
    if(flag==0):
        print(num,"is prime")
