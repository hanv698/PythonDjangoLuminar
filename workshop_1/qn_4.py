str=input("Enter string:")
first=input("First letter:")
sec=input("Second letter:")

f=0
flag=0

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