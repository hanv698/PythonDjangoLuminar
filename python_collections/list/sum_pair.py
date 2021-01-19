list_1=[]
n=int(input("Enter range:"))
print("Enter elements:")
for i in range(0,n):
    num=int(input())
    list_1.append(num)

low=0
up=len(list_1)-1

element=int(input("Enter sum to find pair:"))
list_1.sort()

while(low<up):
    total=list_1[low]+list_1[up]
    if(element==total):
        print("(",list_1[low],list_1[up],")")
        low+=1
        #break
    elif(element>total):
        low+=1
    elif(element<total):
        up-=1