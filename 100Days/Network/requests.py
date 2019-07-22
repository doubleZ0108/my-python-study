from threading import Thread
import requests

class DownloadHandler(Thread):
    def __init__(self, url, title):
        super().__init__()
        self._url = url
        self._title = title

    def run(self):
        # filename = self._url[self._url.rfind('/')+1:]
        resp = requests.get(self._url)
        with open('Users/' + self._title + '.jpg', 'wb') as f:
            f.write(resp.content)

def main():
    '''
    通过requests模块的get函数获取网络资源
    '''
    resp = requests.get('http://api.tianapi.com/meinv/?key=APIKEY&num=10')
    data_model = resp.json()
    print(data_model)
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        title = mm_dict['title']
        # 通过多线程的方式下载图片
        DownloadHandler(url, title).start()


if __name__ == '__main__':
    main()
