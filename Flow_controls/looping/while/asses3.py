#3-3+33+333 program

num=int(input("Enter num(1-9):"))
i=1
sum=0 #data=0
j=0
pattern=""
while(i<=num): #int(num)
    j=(j*10)+num #res=num*i
    sum=sum+j #date+=int(res)
    i+=1
print(":",sum)

