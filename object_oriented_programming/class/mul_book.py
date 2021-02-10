class Book(object):
    def __init__(self,pages):
        self.pages=pages

    def __mul__(self,other):
        return Book(self.pages*other.pages)

    def __str__(self):
        return str(self.pages)

obj=Book(100)
obj1=Book(2)
obj2=Book(100)

print(obj*obj1*obj2)