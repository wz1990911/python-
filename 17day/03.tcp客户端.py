from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("192.168.56.1",8080))
cotent = input("请输入内容")
s.send(cotent.encode("gb2312"))
while True:
    msg = s.recv(1024)
    print(msg.decode("gb2312"))
