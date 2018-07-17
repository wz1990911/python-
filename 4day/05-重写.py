class dog():
    def jiao(self):
        print("汪汪汪")
class erha(dog):
    def jiao(self):
        print("啊呜")
class xiaotianquan(erha):
    def jiao(self):
        print("狂叫")
eh = erha()
xitq = xiaotianquan()
eh.jiao()
xitq.jiao()
