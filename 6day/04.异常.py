class a():
    def shu(self):
        try:
            a = int(input("请输入数字"))
        except Exception as ret:
            print(ret)
            print("哈哈报错")
        else:
            print(a+1)
class print_1():
    def shu_1(self):
        haha = input("请输入数字")
        l = haha.isdigit()
        if l == False:
            print("错误")
        else:
            print(int(haha)+1)
b = a()
b.shu()
c = print_1()
c.shu_1()
       
