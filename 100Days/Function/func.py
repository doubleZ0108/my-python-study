# 函数的高阶用法
'''
将函数视为“一等公民”
    1.函数可以赋值变量
    2.函数可以作为函数的返回值
    3.函数可以作为函数的参数
'''

def hi(name='zz'):
    print('hi ' + name)
greet = hi  # 注意这里没有小括号
greet()

del hi
# hi()    # NameError: name 'hi' is not defined
greet()

''''''''''''''''''''''''''''''''''''

def outer(name='zz'):
    def inner_zz():
        return 'you are in the inner_zz()'
    def inner_yt():
        return 'you are in the inner_yt()'
    if name=='zz':
        return inner_zz # 如果加小括号,函数就会被执行, 这样不加就可以到处被传递
    else:
        return inner_yt

foo = outer()   # 赋值的时候就已经执行了一层了
print(foo)  # <function outer.<locals>.inner_zz at 0x108ff0830>
print(foo())    # you are in the inner_zz()
print(outer('yt')())    # you are in the inner_yt()

''''''''''''''''''''''''''''''''''''
def you():
    return 'this is you()'

def me(you):
    print('this is me()')
    print(you())

me(you) # 同样,这里的you是参数, 因此不能让他执行
