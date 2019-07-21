from multiprocessing import Process,Lock
from time import time, sleep
from os import getpid
from random import randint
from threading import Thread

class DownloadTaskHandler(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
    
    def run(self):
        print('%s下载开始...进程号[%d]' % (self._filename,getpid()))
        time_to_download = randint(1,6)
        sleep(time_to_download)
        print('%s下载完成, 耗时%d' % (self._filename, time_to_download))


if __name__ == "__main__":
    start = time()
    dh1 = DownloadTaskHandler('file1')
    dh1.start()
    dh2 = DownloadTaskHandler('file2')
    dh2.start()
    dh1.join()
    dh2.join()
    end = time()
    print("共耗时%.2f" % (end-start))
