# map -> 根据提供的函数对指定的序列进行映射
'''
map(function, iterable, ...)
    第一个参数 function 以参数序列中的每一个元素调用 function 函数
    python2返回新列表
    python3返回迭代器
'''
## 计算列表各个数的平方
def square(x):
    return x**2
print(list(map(square,[1,2,3,4,5])))    # map的返回值是map object，将其转换为list

## 使用lambda表达式
for item in map(lambda x:x**2, [1,2,3,4,5]):
    print(item)

it = map(square,[1,2,3,4,5])
while True:
    try:
        print(next(it))
    except StopIteration:
        break;

## 对应位置上的元素相加
print(list(map(lambda x,y: x+y,[1,2,3],[4,5,6])))
