# 函数装饰器
## 日志
from functools import wraps

def logging(logfile='log.txt'):
    def logging_decorate(fn):
        @wraps(fn)
        def wrapped_func(*args, **kwargs):
            log_str = fn.__name__ + " was called"
            with open(logfile,'a') as f:
                f.write(log_str + '\n')
            return fn(*args, **kwargs)
        return wrapped_func
    return logging_decorate

@logging()  # 写入默认日志文件(这个小括号是必须的)
def myfunc1(a,b):
    c = a + b
    print(c)

myfunc1(1,2)

@logging('myfunc2_log.txt')
def myfunc2(a,b):
    c = a * b
    print(c)
    
myfunc2(1,2)
