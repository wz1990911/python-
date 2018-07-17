class gongju():
    count = 0
    def __init__(self,name):
        gongju.count+=1
        self.name = name
    def xie(self):
        print("写东西")
    @classmethod
    def getcount(cls):
        return cls.count
a = gongju("铅笔")
b = gongju("钢笔")
a.xie()
b.xie()
print(gongju.getcount())
print(a.getcount())
