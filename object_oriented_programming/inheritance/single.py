class Parent:
    def m1(self):
        print("Inside parent")

class Child(Parent):
    def m2(self):
        print("Inside child")

obj=Child()
obj.m2()
obj.m1()
