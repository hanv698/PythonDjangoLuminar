list_1=[]
n=int(input("Enter range:"))
print("Enter elements:")
for i in range(0,n):
    num=int(input())
    list_1.append(num)

list_1.sort()

element=int(input("Enter element to be searched:"))

beg=0
last=len(list_1)-1
while(beg<=last):
    mid=(beg+last)//2
    if(element>list_1[mid]):
        beg=mid+1
    elif(element<list_1[mid]):
        last=mid-1
    elif(element==list_1[mid]):
        flag=1
        break
if(flag==1):
    print("Element found at",mid+1)
else:
    print("Element not found")
