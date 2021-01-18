#lst=[1,2,3,4,5]

lst=[]
print("Enter elements:")
for i in range(0,5):
    n=int(input())
    lst.append(n)

num=int(input("Enter the sum to be searched:"))

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if((lst[i]+lst[j])==num):
            print("(",lst[i],",",lst[j],")")

