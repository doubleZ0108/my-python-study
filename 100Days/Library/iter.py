# 迭代器
'''
iter()从可迭代的对象返回一个迭代器
next()从迭代器中取下一条记录，只能往后取，不能取回去

延迟计算或惰性求值 (Lazy evaluation)
    迭代器不要求你事先准备好整个迭代过程中所有的元素。仅仅是在迭代至某个元素时才计算该元素，
    而在这之前或之后，元素可以不存在或者被销毁。
    这个特点使得它特别适合用于遍历一些巨大的或是无限的集合。
'''

li = [1,2,3,4,5]
it = iter(li)

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break;

## 也可以用for进行遍历
## 但要注意此时什么都不会输出，因为迭代器已经到尾了
for item in it:
    print(item)


# 自定义迭代器
class myList(object):
    def __init__(self, li):
        self._li = li
        self._current = 0
    
    @property
    def len(self):
        return len(self._li)

    # 方法返回一个特殊的迭代器对象，这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成
    def __iter__(self):
        self._current = 0
        return self
    
    def __next__(self):
        if self._current<self.len:
            x = self._li[self._current]
            self._current += 1
            return x
        else:
            raise StopIteration

myli = myList([1,2,3,4,5])
myit = iter(myli)

while True:
    try:
        print(next(myit))
    except StopIteration:
        break;
