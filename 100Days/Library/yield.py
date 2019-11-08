'''
yield
可以像list那样遍历, 又不占用多少内存
generator是一种特殊的迭代器, 只能被遍历一次, 遍历结束就自动消失, 从而减少内存消耗
'''
def get_square(n):
    result = list()
    for i in range(n):
        result.append(i**2)
    return result

def get_square_with_yield(n):
    for i in range(n):
        yield(i**2)

if __name__ == "__main__":
    a = get_square(5)
    b = get_square_with_yield(5)

    for item in a:
        print(item, end=' ')
    print()
    for item in b:
        print(item, end=' ')