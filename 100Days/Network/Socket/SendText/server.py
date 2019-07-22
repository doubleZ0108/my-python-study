from socket import socket, SOCK_STREAM, AF_INET

def main():
    '''
    1.创建TCP套接字对象
    family=AF_INET --> IPv4地址
    family=AF_INET6 --> IPv6地址
    '''
    server = socket(family=AF_INET, type=SOCK_STREAM)
    '''
    2.绑定IP地址和端口
    (同一时间一个端口上只能绑定一个服务)
    '''
    server.bind(('192.168.223.1', 6789))
    '''
    3.开启监听
    (监听客户端连接到服务器)
    参数512可以理解为连接队列的大小
    '''
    server.listen(512)
    print('服务器启动开始监听...')

    while True:
        '''
        4.通过循环接受客户端的连接并作出相应的处理(提供服务)
        accept方法为阻塞方法, 如果没有客户端连接到服务器代码不会向下执行
            返回值的第一个元素是客户端对象
                   第二个元素是连接到服务器的客户端的地址(IP+端口)
        '''
        client, addr = server.accept()
        print(str(addr) + '连接到服务器')
        '''
        5.发送数据
        '''
        client.send('I love you\n           -- from double Z'.encode('utf-8'))
        '''
        6.断开连接
        '''
        client.close()

if __name__ == "__main__":
    main()
