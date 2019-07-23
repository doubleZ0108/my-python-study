from socket import socket
from base64 import b64encode
from json import dumps
from threading import Thread

class FileTransHandler(Thread):
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
    server = socket()
    server.bind(('192.168.223.1',7890))
    server.listen(512)
    print('服务器开始监听...')

    with open('Resources/img.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')

    while True:
        client, address = server.accept()
        print(str(address) + '连接到服务器')
        FileTransHandler(client, data, 'img').start()





if __name__ == "__main__":
    main()
