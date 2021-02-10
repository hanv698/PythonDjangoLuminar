from re import *

cnt=0
pattern="aba"

matcher=finditer(pattern,"abababababababa")

for match in matcher:
    print(match.start(),"-->",match.group())
    cnt+=1
print("Count:",cnt)