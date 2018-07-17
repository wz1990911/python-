import random
class you():
    def cai(self):
        a = random.randint(1,100)
        while True:
            b = int(input("请输入数字"))
            if b < a:
                print("数字小了")
            elif b > a:
                print("数字大了")
            else:
                print("猜中了")
                break
ren = you()
ren.cai()
