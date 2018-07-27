def w1(fun):
    def inner(*args,**kwargs):
        print("验证成功")
        fun(*args,**kwargs)
    return inner
@w1
def play1():
    print("哈哈哈哈")
play1()
@w1
def play2(a):
    print("哈哈哈哈%s"%a)
play2("额")
@w1
def play3():
    return "啦啦啦啦"
ret=play3()
print(ret)
