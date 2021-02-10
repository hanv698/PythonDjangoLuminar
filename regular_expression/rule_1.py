from re import *

variable_name=input("Enter Variable name")

rule="[a-k][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,variable_name)

if matcher==None:
    print("Invalid Pattern")

else:
    print("Valid Pattern")