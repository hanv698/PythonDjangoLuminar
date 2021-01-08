import mathpack.MyMathFunctions
add=mathpack.MyMathFunctions.add(10,20)
print("Sum:",add)
print("------")
from mathpack.MyMathFunctions import *
print("Sum:",add(50,50))
print("Diff:",sub(50,30))
print("Prod:",mul(50,30))
print("Quo:",div(20,10))