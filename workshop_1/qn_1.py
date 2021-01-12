n=int(input("Enter the number of rows in the * triangle:"))
c=((n-1)*2)-1

if(n>2):
    for row in range(1,n+1):
        for col in range(1,c+1):
            if((row==n)|(col+row==n)|(col-row==n-2)):
                print("*",end="")
            else:
                print(end=" ")
        print()
else:
    print("INVALID")