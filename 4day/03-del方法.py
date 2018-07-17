class dag():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "我的名字是%s"%self.name
    def __del__(self):
        print("哈哈哈")
    def xing(self):
        print("汪汪汪")
tom = dag("tom")
tom1 = tom
del tom
del tom1
print("hahahah")
