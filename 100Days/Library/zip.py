# zip -> 将对象中各个元素打包成一个个元组
# zip后的值不会改变, 但是都会变成元组(除非长度不一致)
a = [1,2,3]
zipped = zip(a)
print(list(zipped))     # [(1,), (2,), (3,)]


b = [4,5,6]
zipped = zip(a,b)
print(list(zipped))     # [(1, 4), (2, 5), (3, 6)]

c = 'zhang'
zipped = zip(a,b,c)
print(list(zipped))     # [(1, 4, 'z'), (2, 5, 'h'), (3, 6, 'a')]  元素个数与最短的列表一致


x = zip(*zip(a,b,c))    # 这块写zip(*zipped)就输出[], 不知道为什么
print(list(x))          # [(1, 2, 3), (4, 5, 6), ('z', 'h', 'a')] 可以理解为压缩
