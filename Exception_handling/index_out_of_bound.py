lst=[10,20,30]
pos=int(input("Position:"))

try:
    print(lst[pos])
except Exception as e:
    print("Index Out of Bound")