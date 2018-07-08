import os
class chuang00
def xuan():
    while True:
        print("1------创建文件")
        print("2------备份文件")
        print("3------批量文件重命名")
        print("4------查看文件")
        print("5------删除文件")
        print("0------退出")
        a = int(input("请选择"))
        if a == 1:
            print_1()
        elif a == 2:
            print_2()
        elif a == 3:
            print_3()
        elif a == 4:
            print_4()
        elif a == 5:
            print_5()
        elif a == 0:
            break
def print_1():
    name = input("请输入你要创建的文件ming")
    f = open("name","w")
    content = input("请输入你要写的内容")
    f.write(content)
    input("输入成功")
def print_2():
    name = input("请输入你要备份文件的名字")
    f = open("name","r")
    content = f.read()
    a = name.rfind(".")
    name_2 = name[:a]+"back"+name[a:]
    f1 = open("name_2","w")
    f1.write(content)
    print("备份成功")
    f.close()
    f1.close()
def print_3():
    name = input("请输入你要批量重命名的文件夹")
    a = os.listdir(name)
    os.chdir(name)
    name_1 = input("请输入你要添加的名字")
    for i in a:
        os.rename(i,name_1+i)
def print_4():
    name = input("请输入你要查看的文件")
    f = open("name","r")
    content = f.read()
    print(content)
def print_5():
    name = input("请输入你要删除的文件")
    os.remove(name)
    print("删除成功")
xuan()
