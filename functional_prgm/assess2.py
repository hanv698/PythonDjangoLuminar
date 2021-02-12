lst1=[1,2,3,4,5,6]

lst2=[]
print("Enter elements:")
for i in range(0,6):
    num=int(input())
    lst2.append(num)
print(lst2)

x=lst2[len(lst2)-1]
y=lst2[0]
z=lst2[1]

flag=0

for i in lst1:
    if i==y:
        if i-1==x and i+1==z:
            flag=1
            break

if flag==1:
    print("rotation")
else:
    print("not rotation")

