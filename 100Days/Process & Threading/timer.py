'''
定时器
'''
from threading import Timer
from time import sleep

def myclock():
    print('hello world!')

    # 要将这三句写在函数的最后
    global timer
    timer = Timer(1,myclock)    # 之后每隔1s调用一次函数
    timer.start()


timer = Timer(0,myclock).start()    # 0时刻启动定时器

sleep(5)        # 5s中之后（非阻塞）
timer.cancel()  # 取消定时器
print('The timer is cancel')
