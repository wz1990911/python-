tus = []#定一个空列表 来装输入的名字
while True:
    fun = int(input("1---添加 2--删除 3---改 4---查(把素以打印出来)"))
    if fun == 1:
        name = input("请输入名字")
        stus.append(name)
    elif fun == 2:
        '''
        先查一下你在不在列表当中，如果在，就可以删，不在提示不存在     
        '''
        name = input("请输入你要删除的名字")
        if name in stus:#如果True 一定在
            stus.remove(name)
        else:
            print("查无此人")
    elif fun == 3:
        '''
        先知道旧的名字，去查这个人在不在这个列表里面
        如果在的，通过名字去找索引
        找到索引，就可是输入新的名字进行修改吧
        如果不在，提示没有此人
        '''
        name = input("请输入你要修改人的名字")
        if name in stus:
            position = stus.index(name)
            name = input("请输入新的名字")
            stus[position] = name#修改
        else:
            print("查无此人")
    elif fun == 4:
        name = input("请输入查询的名字")
        if name in stus:
            position = stus.index(name)
            print("你要查的人的索引是%d"%position)
        else:
            print("查无此人") 
    print(stus)

