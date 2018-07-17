class jiu():
    __instance = None
    __first_init = False
    def __new__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,age,name):
        if not self.__first_init:
            self.age = age
            self.name = name
            jiu.__first_inist = True
a = jiu(10,"九妹")
b = jiu(9,"九妹")
print(id(a))
print(id(b))
