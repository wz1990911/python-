import os
name = input("请输入要批量重命名的文件夹")
a = os.listdir(name)
for i in a:
    position = i.rfind(".")
    name_1 = i[:position]+"必属精品"+i[position:]
    os.rename(i,name_1)
