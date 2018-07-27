from threading import Thread
import time
def saySorry():
    time.sleep(1)
    print("哈哈哈")
for i in range(5):
    t = Thread(target = saySorry)
    t.start()

