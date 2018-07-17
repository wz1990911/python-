class ren():
    def __init__(self,name,color = "白色"):
        self.name = name
        self.__money = 1000
        self.color = color
    def setcolor(self,color):
        self.color = color
    def getMoney(self):
        return self.__money
    def __str__(self):
        msg = "名字是%s颜色是%s"%(self.name,self.color)
        return msg
    def chi(self):
        print("吃东西")
    def wan(self):
        print("玩游戏")
    def shui(self):
        print("睡觉")
class nanren(ren):
    pass
nan = nanren("波斯猫","黑色")
print(nan.getMoney)
nan.chi()
nan.wan()
nan.shui()
print(nan)
