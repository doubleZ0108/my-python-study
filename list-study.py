## 列表
list = [1,3,5,7,100]
list2 = ['hello']*5

# 添加元素
list.append(200)
list.insert(1,400)
print(list)

# 删除元素
list.remove(3)		# 是把值为3的元素删掉，不是3下标的元素
del list[0]		# 删除下标为0的元素




# 复制列表
fresh = list[:]
buf = list # 没有复制列表，只是创建了新的引用
reverse  = list[::-1]	# 获取倒转的列表拷贝

# 排序
sorted_list = sorted(list)	# 返回排序列表后的拷贝，不会修改传入的列表
reverse_sorted_list = sorted(list, reverse=True)
len_sorted_list = sorted(list, key=len)	# 根据字符串的长度进行排序而不是默认的字母表顺序

list.sort()	# 直接在原对象上进行排序




import sys

## 列表的生成式语法，此方法需要消耗较多的内存
f = [x for x in range(1,10)]
print(f)
f = [x+y for x in 'ABCDE' for y in '1234567']
print(f)

f = [x**2 for x in range(1,10)]
print(f)
print(sys.getsizeof(f))		# 查看对象占用内存的字节数

## 创建生成器对象，可以获取到数据但它不占用额外的空间存储数据，每次需要用到数据的时候就再次计算得到（需要花费额外的时间）
f = (x**2 for x in range(1,10))
print(sys.getsizeof(f))
print(f)
for val in f:
	print(val)
	
	
## 将函数改造成生成器函数
# 斐波那契数列
def fib(n):
	a,b = 0,1
	for _ in range(n):
		a,b = b,a+b
		yield a
		
for val in fib(20):
	print(val)
