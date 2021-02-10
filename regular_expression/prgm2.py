from re import *

#pattern="a+"
#pattern="a*"
#pattern="a?"
#pattern="a{3}"
pattern="a{2,4}"

matcher=finditer(pattern,"aaaaabaaababababab")

for match in matcher:
    print(match.start(),"-->",match.group())