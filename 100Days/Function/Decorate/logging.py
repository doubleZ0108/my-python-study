# 函数装饰器
## 日志
from functools import wraps

def logging(fn):
    @wraps(fn)
    def log_decorate(*args, **kwargs):
        print(fn.__name__ + ' was called')
        return fn(*args, **kwargs)
    return log_decorate

@logging
def func(a,b):
    print(a,b)
