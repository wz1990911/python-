import time
from threading import Thread
def sing():
    time.sleep(2)
    print("做你的眼睛 安排~")
for i in range(5):
    t = Thread(target = sing)
    t.start()
print("哈哈")
