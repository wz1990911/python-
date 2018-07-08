name = input("请输入要改的文件名")
f = open(name,'r')
while True:
    if f.read(1024) == "":
        break
    content = f.read(1024)
print(content)
name_1 = name.rfind(".")
a = name[:name_1]+"back"+name[name_1:]
f1 = open(a,'w')
f1.write(content)
f.close()
f1.close()
