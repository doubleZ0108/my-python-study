# 函数装饰器
## 授权
from functools import wraps

def require_auth(fn):
    @wraps(fn)
    def auth_decorate(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authorize()  # 进行授权操作
        return fn(*args, **kwargs)
    return auth_decorate
