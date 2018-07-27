def w1(fun):
    def inner():
        print("验证成功")
        fun()
    return inner
@w1
def test():
    print("-------支付-------")
test()
