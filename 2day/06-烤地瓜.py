import time
class digua():
    def __init__(self):
        self.zhuangtai = "生的"
        self.time = 0
        self.list = []
    def peng(self):
        self.time+=1
        if self.time < 3:
            self.zhuangtai = "生的"
        elif self.time >3 and self.time <10:
            self.zhuangtai = "半生不熟"
        elif self.time < 10  and self.time < 15:
            self.zhuangtai = "熟了"
        elif self.time > 15:
            self.zhuangtai = "糊了"
    def pan(self):
        print(self.zhuangtai)
        print("作料有%s"%self.list)
    def zuoliao(self,s):
        self.list.append(s)
diuxian = digua()
for i in range(15):
    diuxian.peng()
    if i == 1:
        diuxian.zuoliao("盐")
    elif i == 2:
        diuxian.zuoliao("糖")
    elif i == 3:
        diuxian.zuoliao("醋")
    diuxian.pan()
    time.sleep(1)
