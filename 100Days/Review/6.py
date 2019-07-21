from multiprocessing import Process,Lock
from time import time, sleep
from os import getpid
from random import randint

def Download_Task(filename):
    print('%s下载开始...进程号[%d]' % (filename,getpid()))
    time_to_download = randint(1,10)
    sleep(time_to_download)
    print('%s下载完成, 耗时%d' % (filename, time_to_download))

if __name__ == "__main__":
    start = time()
    p1 = Process(target=Download_Task, args=('file1',))
    p1.start()
    p2 = Process(target=Download_Task, args=('file2',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print("共耗时%.2f" % (end-start))
