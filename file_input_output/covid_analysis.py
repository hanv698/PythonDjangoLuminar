f=open("covid_19_india.csv","r")

dict={}

for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3].rstrip("***")
    confirmed_cases=int(data[8])

    if(state=="Telengana"):
        state="Telangana"

    if(state not in dict):
        dict[state]=confirmed_cases
    else:
        dict[state]=confirmed_cases


for k,v in dict.items():
    print(k,":",v)
print("==========================")

res=sorted(dict,key=dict.get,reverse=True)
print(res)
print("==========================")
print(res[0],":",dict[res[0]])
print("==========================")
result=sorted(dict)
print(result)