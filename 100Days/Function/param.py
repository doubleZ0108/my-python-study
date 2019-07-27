# 函数高阶用法

'''
1.位置参数
参数的顺序必须一一对应，且少一个参数都不可以

2.关键字参数
可以不用关心参数的顺序

3.默认参数
注意：所有位置参数必须出现在默认参数前，包括函数定义和调用

4.可变参数
    包裹位置传递
    包裹关键字传递
'''

def func1(name, age):
    print(f'This is {name}, he is {age} years old.')
func1(age=50,name='zz')

def func2(*argv):
    for var in argv:
        print(var)
func2(1)
func2(1,2,3)

def func3(**kargv):
    for key,value in kargv.items():
        print(f'({key},{value})')
func3(a=1)
func3(a=1,b=2,c=3)
# func3(1)    # 调用时不能传递位置参数 TypeError: func3() takes 0 positional arguments but 1 was given


'''
参数的元信息:
    添加的元信息不会做任何检查
    只是对使用者做提示, 写代码时弹出的小框框会显示

    函数注解置存储在函数的__annotations__属性中
'''
def myadd(x:int, y:int) -> int:
    return x+y
print(myadd.__annotations__)    # {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}


