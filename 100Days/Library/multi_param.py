'''
* --> 可变参数
'''
def multi_sum(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

'''
** -> 键值对可变参数
'''
def foo(**kwds):
    for key in kwds:
        print(key, kwds[key])

if __name__ == "__main__":
    print(multi_sum(1,3,5,7,9))
    foo(name='zz', age=19)