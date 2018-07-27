from multiprocessing import Process
import time
def work(arg):
    for i in range(10):
        time.sleep(1)
        print("呵呵",arg)
p = Process(target = work,args=("哈哈",))
p.start()#开启子进程
p.join(3)#等待子进程执行完毕 超时自己出来
print("我是主进程")

