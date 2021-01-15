list_1=[]
print("Enter elements:")
for i in range(0,3):
    num=int(input())
    list_1.append(num)

list_2=[]

for i in range(0,len(list_1)):
    if(i==0):
        list_2.append(list_1[i+1]+list_1[i+2])
    elif(i==1):
        list_2.append(list_1[i+1]+list_1[i-1])
    else:
        list_2.append(list_1[i-1]+list_1[i-2])
print("list_2:",list_2)
