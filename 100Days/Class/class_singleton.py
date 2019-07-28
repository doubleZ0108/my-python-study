# 元编程和元类
## 用元类实现单例模式

from threading import Lock

class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        cls.__lock = Lock()
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

class President(metaclass=SingletonMeta):
    pass

ps = []
for _ in range(5):
    p = President()
    ps.append(p)

for p in ps:
    print(id(p))    # 都是同样的id
