# 函数的参数
## 可变参数（个数是不确定的）
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add(1,2,3));
print(add(1,2,3,4,5));


## 将两个数排序
x = int(input('please input x = '))
y = int(input('please input y = '))
(x,y) = (x,y) if x<y else (y,x)
print(x,y);


## 判断回文数
def isPalindrome(num):
    temp = num
    total = 0
    while temp:
        total = total * 10 + temp % 10
        temp //= 10     # 两个//是整除
    return total == num

num = int(input('please input num = '))
print(isPalindrome(num))


# 作用域
def func():
    b = 'hello world'   # 嵌套作用域

    def bar():
        c = True    # 局部作用域
        print(a)
        print(b)
        print(c)

    bar();
if __name__=="__main__":
    a = 123     # 全局作用域 -> 在函数内部无法修改全局的东西
    func();

def func():
    global a    # 全局变量
    a = 200
    print(a)

if __name__=="__main__":
    a=100
    func();
    print(a)
