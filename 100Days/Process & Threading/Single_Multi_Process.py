from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


def download_task(filename, multi_threading = False):
    if multi_threading:
        print('启动下载进程, 进程号[%d]' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成, 耗时%ds' % (filename, time_to_download))


def Single_Threading():
    start = time()
    download_task('Python程序设计')
    download_task('离散数学')
    end = time()
    print('单进程执行共耗时: %.2f' % (end-start))


'''
Process --> 创建了进程对象
target --> 一个函数, 表示进程启动后要执行的代码
args --> 一个元组, 代表传递给函数的参数
start() --> 启动进程
join() --> 等待进程执行结束
'''
def Multi_Threading():
    start = time()
    p1 = Process(target = download_task, args=('Python程序设计', True))
    p1.start()
    p2 = Process(target = download_task, args=('离散数学', True))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('多进程执行共耗时: %.2f' % (end-start))



if __name__ == "__main__":
    Single_Threading()
    Multi_Threading()
