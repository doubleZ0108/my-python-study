from socket import socket

def main():
    # 1.创建套接字对象默认使用IPv4和TCP协议
    client = socket()
    # 2.连接到服务器
    client.connect(('192.168.223.1',6789))
    # 3.从服务器接受数据
    reps = client.recv(1024).decode('utf-8')
    print(reps)
    # 4.断开连接
    client.close()

if __name__ == "__main__":
    main()
