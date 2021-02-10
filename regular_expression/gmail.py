from re import *

gmail=input("Enter gmail-id")

rule="[a-z.]+\d*[@]gmail.com"

matcher=fullmatch(rule,gmail)

if matcher==None:
    print("Invalid mail-id")

else:
    print("Valid mail-id")