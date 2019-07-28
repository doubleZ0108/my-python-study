e# 枚举类
from enum import Enum, unique

@unique     # 不能定义相同的成员值
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    # RED, GREEN, BLUE, YELLOW = range(1,4)

    '''
    枚举成员不能进行大小比较
    Color.RED < Color.BLUE      # TypeError: '<' not supported between instances of 'Color' and 'Color'
    正确的做法应该是添加魔法函数, 比较二者的值属性大小
    '''
    def __lt__(self, other):
        return self.value<other.value


print(Color['BLUE'])    # Color.BLUE 通过成员名来获取成员
print(Color(3))         # Color.BLUE 通过成员值来获取成员

# 每个成员都有名称属性和值属性
member = Color.GREEN
print(member.name)      # GREEN
print(member.value)     # 2

# 遍历成员
for color in Color:
    print(color)

# 将名称映射到成语啊 的有序字典
for color in Color.__members__.items():
    print(color)    # ('RED', <Color.RED: 1>)

print(Color.RED < Color.BLUE)
