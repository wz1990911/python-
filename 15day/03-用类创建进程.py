from multiprocessing import Process
import time 
class Myprocess(Process):
    def __init__(self,name):
        super().__init__() #初始化父类给我们提供的一些功能
        self.name = name
    def run(self):
        for i in range(10):
            time.sleep(1)
            print("我重写了run方法%s"%(self.name))
p = Myprocess("老王")
p1 = Myprocess("老宋")
p.start()
p1.start()
p.join()
p1.join()
print("我是主线程")
