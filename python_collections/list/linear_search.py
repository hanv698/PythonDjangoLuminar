lst=[10,20,30,40,50]
element=int(input("Enter element to be searched:"))
flag=0
count=0

for i in lst:
    if(element==i):
        flag=1
        break

    else:
        pass
    count += 1
if(flag==1):
    print("Element found at",count+1)
else:
    print("Element not found")