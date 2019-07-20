from threading import Thread
from time import time, sleep
from random import randint

class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    # run()在start()之后自动执行
    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5,10)
        sleep(time_to_download)
        print('%s下载完成, 耗时%ds' % (self._filename, time_to_download))


if __name__ == "__main__":
    start = time()
    t1 = DownloadTask('Python程序设计')
    t1.start()
    t2 = DownloadTask('离散数学')
    t2.start()
    t1.join()
    t2.join()
    end = time()

    print('多进程执行共耗时: %.2f' % (end-start))
