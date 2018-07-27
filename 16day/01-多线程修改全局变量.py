from threading import Thread,Lock
import time
num = 0
flag = 1
def work1():
    global num
    for i in range(1000000):
        mutex.acquire(True)
        num+=1
        mutex.release()
    print(num)
def work2():
    global num
    for i in range(1000000):
        mutex.acquire(True)
        num+=1
        mutex.release()
    print(num)
mutex = Lock()
t = Thread(target = work1)
t1 = Thread(target = work2)
t.start()
t1.start()
