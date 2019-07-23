from threading import Thread
import requests
import os

class DownloadImgHandler(Thread):
    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename
    
    def run(self):
        resp = requests.get(self._url)

        curr_dir = os.getcwd()
        save_path = curr_dir + '\\Img\\'
        if not os.path.exists(save_path):
            os.mkdir(save_path)

        with open(save_path + self._filename + '.jpg', 'wb') as f:
            f.write(resp.content)

def main():
    Img_urls = [
        'https://www.apple.com/v/home/ek/images/heroes/iphone-xs/main__bmngiblug0mq_small_2x.jpg',
        'https://www.apple.com/v/home/ek/images/logos/series_4__b539g9eyf22u_large_2x.jpg',
        'https://www.apple.com/v/home/ek/images/promos/ipad-pro/ipad_pro__cesqtbwwmi2u_large_2x.jpg',
        'https://www.apple.com/v/home/ek/images/promos/macbook-air/macbook_air__knzp0i282eyy_small_2x.jpg',
    ]

    index = 0
    for Img_url in Img_urls:
        DownloadImgHandler(Img_url, 'Img'+str(index)).start()
        index += 1


if __name__ == "__main__":
    main()
