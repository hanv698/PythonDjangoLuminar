line="hello hai hello hai hello"

word=line.split(" ")

dict={}

for i in word:
    dict[i]=word.count(i)
print(dict)

#if(i not in dict):
#    dict[i]=1
#else:
#dict[i}+=1


