# 混入 Mixin
## 自定义字典限制只有在指定的key不存在时才能在字典中设置键值对

import traceback

class SetOnceMappingMixin():
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key,value)


class SetOnceDict(SetOnceMappingMixin, dict):
    pass

my_dict = SetOnceDict()
try:
    my_dict['username'] = 'zz'
    my_dict['username'] = 'yt'
except KeyError:
    traceback.print_exc()   # 跟踪错误
print(my_dict)
