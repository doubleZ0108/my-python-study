# 用装饰器实现单例模式
## 通过锁实现线程安全的单例模式

from functools import wraps
from threading import Lock

def singlenton(cls):
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singlenton
class President():
    pass

ps = []
for _ in range(5):
    p = President()
    ps.append(p)

for p in ps:
    print(id(p))    # 都是同样的id
