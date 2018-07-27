from socket import *
s = socket(AF_INET, SOCK_DGRAM)
#s.bind(("",8888))
s.sendto("哈哈哈".encode("gb2312"),("192.168.56.1",8080))
while True:
    msg = s.recvfrom(1024)
    print("消息是:%s 来自ip:%s"%(msg[0].decode('gb2312'),msg[0][1]))
s.close()
