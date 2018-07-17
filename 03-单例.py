class dog():
    __instance = None
    __flag = False
    def __new__(cls,*args,**kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self,name):
        if dog.__flag == False:
            self.name = name
            dog.__flag = True
        
a = dog("a1")
print(id(a))
b = dog("b1")
print(id(b))
