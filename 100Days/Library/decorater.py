'''
装饰器
timer时我们定义的装饰器函数, 可以用@把它附加到任何函数定义之前, 相当与把该函数做成装饰器函数的输入参数
调用do_something时相当于掉用timer(do_something)
'''
import time

def timer(func):
    def wrapper(*args, **kwds):
        start = time.time()
        func(*args, **kwds)
        end = time.time()
        print('cost %.3f s' % (end-start))
    return wrapper

@timer
def do_something(delay):
    print('start do something...')
    time.sleep(delay)
    print('end do something...')

if __name__ == "__main__":
    do_something(2)