f=open("movies.csv","r")

dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    count=0
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1

for k,v in dict.items():
    print(k,":",v)

print("***********************")

maxi=sorted(dict,key=dict.get,reverse=True)
print(maxi[0],":",dict[maxi[0]])