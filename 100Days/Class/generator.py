f = (x**2 for x in range(1,11)) # 这是一个生成器，不占用空间存储，每次使用都重新计算
print(f)
for val in f:
    print(val,end=' ')

"""
1.带有 yield 的函数不再是一个普通函数，而是一个生成器generator
2.yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。
3.重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。
4.简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
"""

## 斐波那契数列
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        yield a

for val in fib(20):
    print(val)
