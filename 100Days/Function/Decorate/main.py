from functools import wraps
# 函数装饰器

'''
执行效果相当于: funB = funA(funB) & print(funB)
    1.funA(funB) --> 输出this is A
    2.执行fn(), 相当于调用了真正的funB --> 输出this is B
    3.将funB替换为funA的返回结果, 现在funB变成一个字符串了
'''
def funA(fn):
    print('this is A')
    fn()
    return 'doubleZ'

@funA
def funB():
    print('this is B')

print(funB)


'''
执行效果相当于: func = check(func(1,2))
    1.check(func(2,3)) --> 直接返回check_fn
    2.现在func相当于check_fn
    3.先进行检查,再执行原来的加法逻辑

@wraps复制函数名称, 注释文档, 参数列表等
还可以让我们再装饰器里面访问再装饰之前的函数属性
(如果不加这个的话 func.__name__就是check_fn了)
'''
def check(fn):

    @wraps(fn)
    def check_fn(*args):
        print('=====这里模拟进行运行前的检查=====')
        fn(*args)
        print('=====这里模拟进行运行后的检查=====')
    return check_fn

@check
def func(a,b):
    c = a + b
    print(c)

func(1,2)   
print('func.__name__ is ' + func.__name__)
# Output:
# =====这里模拟进行检查=====
# 3
# =====这里模拟进行运行后的检查=====
# func.__name__ is func
