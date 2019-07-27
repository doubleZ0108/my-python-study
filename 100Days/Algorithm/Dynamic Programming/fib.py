'''
动态规划法

斐波那契

主要欣赏下python备忘录的简单使用方法
'''

def fib(num, memo={}):
    if num in (0,1,2):
        return 1
    try:
        return memo[num]
    except KeyError:
        memo[num] = fib(num-2) + fib(num-1)
        return memo[num]

if __name__ == "__main__":
    for i in range(20):
        print(fib(i))
