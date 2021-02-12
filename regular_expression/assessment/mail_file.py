from re import *

f1=open("mail", "r")
f2=open("mail_valid", "w")

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

for lines in f1:
    data=lines.rstrip("\n")
    matcher=fullmatch(regex,data)

    if matcher==None:
        #print("Invalid mail-id")
        pass

    else:
        f2.write(data)
        f2.write("\n")
        #print("Valid mail-id")