f1=open("vehicle_reg_no","r")
f2=open("vehicle_reg_no_valid","w")

from re import *

#rule="kl[0-9]{2}[a-zA-Z]{2}[0-9]{4}"
rule="kl\d{2}[a-zA-Z]{2}\d{4}"

for lines in f1:
    data=lines.rstrip("\n")
    matcher=fullmatch(rule,data)

    if matcher==None:
        pass
        #print("Invalid registration no")

    else:
        f2.write(data)
        f2.write("\n")
        #print("Valid registration no")