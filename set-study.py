## 集合
# 不允许有重复元素
s = {1,2,3,3,3,2}
print(s)
print(len(s))

# 添加元素
s.add(4)
s.update([11,12])

# 删除元素
s.discard(4)
s.remove(2)		# remove的元素不存在会引发KeyError

fresh = set((1,2,3,3,2,1))	# 将元组转换为集合
print(fresh.pop())
print(fresh)

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
# 交集
print(set1 & set2)		# 自定义运算符
print(set1.intersection(set2))
# 并集
print(set1 | set2)
print(set1.union(set2))
# 差集
print(set1 - set2)
print(set1.difference(set2))
# 对称差（异或）
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 判断子集和超集(真子集)
print(set1 <= set2)
print(set1.issubset(set2))
print(set1 < set2)
print(set1.issuperset(set2))
