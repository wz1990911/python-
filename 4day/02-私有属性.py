class Msg():
    def __sendMsg(self,money):
        if money > 0:
            print("发短信")
        else:
            print("余额不足")
    def sendMsg(self,money):
        self.__sendMsg(money)
msg = Msg()
msg.sendMsg(10)




class shu():
    def __init__(self,name):
        self.__name = name
    def getName(self):
        return self.__name
laowang = shu("老王")
print(laowang.getName())
