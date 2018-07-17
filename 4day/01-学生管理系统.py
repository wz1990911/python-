class student():
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def xuexi(self):
        print("学习")
    def __str__(self):
        return "我的名字是%s我的性别是%s"%(self.name,self.sex)
class Manager():
    def __init__(self):
        self.list = []
    def add(self,student):
        self.list.append(student)
        for i in self.list:
            print(i)
    def remove(self,name):
        for position,i in enumerate(self.list):
            if i.name == name:
                self.list.pop(position)
                print("删除成功")
            else:
                print("查无此人")
    def update(self,name,sex):
        for position,i in enumerate(self.list):
            if i.name == name and i.sex == sex:
                i.name = input("请输入新名字")
                i.sex = input("请输入新性别")
                print("修改成功")
            else:
                print("查无此人") 
    def find(self,name):
       for i in self.list:
            if i.name == name:
                print("我的名字是%s我的性别是%s"%(i.name,i.sex))
            else:
                print("查无此人")
class cai():
    def __init__(self):
        self.m = Manager()
    def print_1(self):
        print("欢迎来到学生管理系统")
        while True:
            print("1------添加")
            print("2------删除")
            print("3------修改")
            print("4------查询")
            print("0------退出")
            fun = int(input("请选择功能"))
            if fun == 1:
                name = input("请输入名字")
                sex = input("请输入性别")
                self.name = name
                self.sex = sex
                s = student(name,sex) 
                self.m.add(s)

            elif fun == 2:
                name = input("输入你要删除的人名")
                self.m.remove(name)
            elif fun == 3:
                name = input("输入你要修改的人名")
                sex  = input("输入你要修改的性别")
                self.m.update(name,sex)
            elif fun == 4:
                name = input("输入你要查找的人名")
                self.m.find(name)
            elif fun == 0:
                break
        
            
m = cai()       
m.print_1()
