from threading import Thread

def Multi_Threading():
    start = time()
    t1 = Thread(target = download_task, args=('Python程序设计'))
    t1.start()
    t2 = Thread(target = download_task, args=('离散数学'))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('多线程执行共耗时: %.2f' % (end-start))
