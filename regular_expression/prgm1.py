from re import *

#pattern='[ab]'
#pattern='[a-z]'
#pattern='[A-Z]'
#pattern='[a-zA-Z]'
#pattern='[0-9]'
#pattern='[^a-zA-Z0-9]'

pattern="\W"

matcher=finditer(pattern,"abc _7ZK@c")

for match in matcher:
    print(match.start(),"-->",match.group())

