from socket import socket

def main():
    server = socket()
    server.bind(('192.168.223.1',7890))
    server.listen(512)

    print('服务器开始监听...')
    while True:
        client, address = server.accept()
        print(str(address) + '连接到服务器')
        client.send('hello world!'.encode('utf-8'))
        client.close()

if __name__ == "__main__":
    main()
