f1=open("phone_no", "r")
f2=open("phone_no_valid", "w")

from re import *

rule = "(91)?\d{10}"

for lines in f1:
    data=lines.rstrip("\n")
    matcher=fullmatch(rule,data)

    if matcher==None:
        pass

    else:
        f2.write(data)
        f2.write("\n")
        #print(lines,"==>Valid mobile no")