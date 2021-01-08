str=input("Enter str:")
rev=""
length=len(str)-1
while(length>=0):
    rev+=str[length]
    length-=1

print(rev)

#for i in range(len(str)):
 #   for j in range(i):
  #      rev+=str[j]

#print(rev)