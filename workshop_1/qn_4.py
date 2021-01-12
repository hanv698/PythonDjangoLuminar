str=input("Enter string:")
first=input("First letter:")
sec=input("Second letter:")
str=str.lower()

f=0
flag=0

if((first in str) & (sec in str)):
    for i in str:
        if(i==first):
            f+=1
        elif(i==sec):
            for j in str:
                if(j==first):
                    flag=1
        str=str.lstrip(i)

    if(flag==0):
        print("True")
    else:
        print("False")
else:
    print("INVALID")