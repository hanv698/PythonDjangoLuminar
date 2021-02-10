lst1=[1,2,3,4]
lst2=[2,4,5,6,8]

common=list(filter(lambda no1:no1 in lst2,lst1))
print(common)