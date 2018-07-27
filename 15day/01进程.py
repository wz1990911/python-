import os
import time
a = 1
p = os.fork()
if p == 0:
    print("我是子进程")
    time.sleep(2)
    print(a)
else:
    a+=1
    print("我是父进程")
    print(a)
