n=int(input("Enter num:"))
min=int(input("Enter min:"))
max=int(input("Enter max:"))
count=0
for i in range(1,(max+1)):
    if i**n in range(min,max+1):
        count+=1
print(count)