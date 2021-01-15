lst=[10,11,12,13,14,15,16,17]
even=[]
odd=[]

for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print(even)
print("Even total:",sum(even))

print(odd)
print("Odd total:",sum(odd))