from socket import socket
from json import loads
from base64 import b64decode

def main():
    '''启动client'''
    client = socket()
    client.connect(('192.168.223.1',6789))

    '''接受数据'''
    in_data = bytes()       # 定义一个保存二进制数据的对象
    data = client.recv(1024)    # 不知道服务器发送的数据有多大, 每次接受1024字节
    while data:
        in_data += data      # 将收到的数据拼接起来
        data = client.recv(1024)
    # 将二进制数据解码成JSON字符串并转换为字典
    my_dict = loads(in_data.decode('utf-8'))
    print(my_dict)
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')

    '''处理数据(储存)'''
    with open('Users/' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存')


if __name__ == "__main__":
    main()
