class lu():
    def eat(self):
        print("吃")
    
class ma():
    def he(self):
        print("喝")
class C(lu,ma):
    pass
luo = C()
luo.eat()
luo.he()
print(C.__mro__)
