class dog():
    def __init__(self):
        print("init")
    def __str__(self):
        print("str")
        return "haha"
    def __del__(self):
        print("del")
    def __new__(cls):
        print("new")
        return object.__new__(cls)
erha = dog()
print(erha)
