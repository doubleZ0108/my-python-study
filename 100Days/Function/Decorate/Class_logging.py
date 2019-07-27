from functools import wraps

class logging(object):
    def __init__(self, logfile='log.txt'):
        self._logfile = logfile
    
    def __call__(self, fn):
        @wraps(fn)
        def wrapped_func(*args, **kwargs):
            log_str = fn.__name__ + " was called"
            with open(self._logfile,'a') as f:
                f.write(log_str + '\n')
            return fn(*args, **kwargs)
        return wrapped_func

@logging('myfunc_log.txt')
def myfunc(a,b):
    c = a + b
    print(c)

myfunc(1,2)
