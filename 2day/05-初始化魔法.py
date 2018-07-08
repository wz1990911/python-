class ren():
    def __init__(self,name,shengao,tizhong):
        self.name = name
        self.shengao = shengao
        self.tizhong = tizhong
    def introduction(self):
        print("我的名字是%s\n我的身高是%d\n我的体重是%dkg"%(self.name,self.shengao,self.tizhong))
nan = ren("王哲",163,50)
nan.introduction()
