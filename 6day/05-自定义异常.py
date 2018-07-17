class haha(Exception):
    def __init__(self,name):
        self.name = name
def main():
    try:
        s = input("请输入名字")
        if s == "老王"
            raise haha(s)
    except haha as result:
        print("报错")
    else:
        print("没有异常")
main()
