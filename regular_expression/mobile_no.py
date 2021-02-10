from re import *

mob_no=input("Enter Mobile no:")

rule="(91)\d{10}"

matcher=fullmatch(rule,mob_no)

if matcher==None:
    print("Invalid mobile no")

else:
    print("Valid mobile no")