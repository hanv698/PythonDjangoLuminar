class Parent:
    def m1(self):
        print("Inside parent")

class Child(Parent):
    def m2(self):
        print("Inside child")

class Subchild(Child):
    def m3(self):
        print("Inside subchild")


obj=Subchild()
obj.m3()
obj.m2()
obj.m1()