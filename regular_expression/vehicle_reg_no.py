#kl2digit2alpha4didit

from re import *

reg_no=input("Enter Registration no:")

#rule="kl[0-9]{2}[a-zA-Z]{2}[0-9]{4}"
rule="kl\d{2}[a-zA-Z]{2}\d{4}"

matcher=fullmatch(rule,reg_no)

if matcher==None:
    print("Invalid registration no")

else:
    print("Valid registration no")