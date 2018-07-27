from multiprocessing import Manager,Pool
import time
def banzhuang(q):
    for i in range(4):
        time.sleep(1)
        q.put("地%d块砖"%i)
        print("放了%d块砖"%i)
def qiqiang(q):
    while True:
        if q.empty() == False:
            for i in range(q.qsize()):
                time.sleep(1)
                print(q.get())
p = Pool() #创建无限大的池子
q = Manager().Queue()#如果用进程池  请用Manager方式创建队列
p.apply_async(banzhuang,(q,))#非阻塞
p.apply_async(qiqiang,(q,))#非阻塞
p.close()
p.join()
