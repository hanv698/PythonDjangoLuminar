str=input("Enter string:")

max=0
for i in str:
    substr=i
    s=str.count(substr)
    if(s>max):
        max=s
        string=i

print(string)


