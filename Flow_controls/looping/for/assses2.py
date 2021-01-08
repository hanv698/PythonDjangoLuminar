num=int(input("Enter num:"))
low_lim=int(input("Enter lower limit:"))
up_lim=int(input("Enter upper limit:"))

for i in range(1,(up_lim+1)):
    if i**num in range(low_lim,up_lim):
        print(i)