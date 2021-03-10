from threading import *
import time

class Myclass:
    def job(self):
        for i in range(10):
            time.sleep(2)
            print("Child thread")

obj=Myclass()
t=Thread(target=obj.job)
t.start()

for i in range(10):
    time.sleep(2)
    print("Main thread class")