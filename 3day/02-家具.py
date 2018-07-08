class fang():
    def __init__(self,acc,area):
        self.acc = acc
        self.area = area
        self.list = []
    def __str__(self):
        jia = "我的家在%s面积有%d"%(self.acc,self.area)
        return jia
    def zhuangjiaju(self,jiaju):
        if self.area < jiaju.area:
            print("装不下了")
        else:
            a.list.append(jiaju)
            self.area -= jiaju.area
            print("面积还剩%d"%self.area)
class tian():
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        jiaju = "名字是%s大小是%d"%(self.name,self.area)
        return jiaju
a = fang("长安街666号",1000)
print(a)
b = tian("席梦思",4)
print(b)
for i in range(300):
    if a.area < b.area:
        print("装不下了")
        break
    else:
        a.zhuangjiaju(b)
