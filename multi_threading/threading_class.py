from threading import *

class Mythread(Thread):
    def run(self):
        for i in range(10):
            print("Inside thread class")

obj=Mythread()
obj.start()

for i in range(10):
    print("Main thread class")