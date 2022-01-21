import socket

# 初始化套接字类
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接到www.py4e.com上的端口80
mysock.connect(('data.pr4e.org',80)) 
# 创建get命令，\r\n表示行尾（回车和转行），\r\n\r\n表示下一行为空
# encode（）将字符串转换为字节对象
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# 套接字发送命令
mysock.send(cmd)

while True:
    # 接受512个字节内的返回值
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # 输出（以空字符串结尾的）返回值
    # decode（）方法将字节对象转换为字符串
    print(data.decode(),end='')

mysock.close()