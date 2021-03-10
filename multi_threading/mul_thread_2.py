import threading
import time

def display():
    for i in range(1,11):
        time.sleep(2)
        print(i,"child thread executing")
        print("-------------------------")
    print(threading.currentThread().getName())

t=threading.Thread(target=display)
t.start()
begintime=time.time()
t.join()

for i in range(1,11):
    time.sleep(2)
    print(i,"main thread executing")
    print("-------------------------")
print(threading.currentThread().getName())

endtime=time.time()
total=endtime-begintime
print(total)