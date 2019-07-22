'''
使用JSON作为数据传输的格式, 但是JSON不能携带二进制数据
因此对二进制数据进行Base64编码处理

Base64时使用64个字符表示所有二进制数据的编码方式
将二进制数据每6位一组组织
刚好可用 0~9a~zA~Z+/ 共64个字符表示 000000到111111 的64种状态
'''
from socket import socket
from base64 import b64encode
from json import dumps
from threading import Thread

class FileTransferHandler(Thread):
    def __init__(self, client, data, filename):
        super().__init__()
        self._client = client
        self._data = data
        self._filename = filename

    def run(self):
        my_dict = {}
        my_dict['filename'] = self._filename
        my_dict['filedata'] = self._data
        json_str = dumps(my_dict)
        self._client.send(json_str.encode('utf-8'))
        self._client.close()

def main():
    '''启动server'''
    server = socket()
    server.bind(('192.168.223.1',6789))
    server.listen(512)
    print('服务器启动开始监听...')


    '''准备待传输的图片数据'''
    file_path = 'Resources/video.mp4'
    file_name = 'video.mp4'
    with open(file_path, 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')


    '''响应客户端'''
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到服务器')
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client, data, file_name).start()

if __name__ == "__main__":
    main()
