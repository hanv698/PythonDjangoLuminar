f=open("demo","r")

dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1

maxi=sorted(dict,key=dict.get,reverse=True)
print(maxi[0],":",dict[maxi[0]])
