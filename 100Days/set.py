# 数据结构
## 集合
set1 = {1,2,1,1,2,3}    # 去重
len(set1)               # [Output]: 3
set2 = set(range(1,11))

### 添加元素
set1.add(4)
set1.add(3)
set2.update([11,12])
### 删除元素
set2.discard(5)
set2.discard(100)
# set2.remove(888)    # remove的元素如果不存在会引发KeyError
set1.pop()  # 删除第一个元素 -> 1


## 集合运算
# 交
set1 & set2
set1.intersection(set2)
# 并
set1 | set2
set1.union(set2)
# 差
set1 - set2
set1.difference(set2)
# 对称差
set1 ^ set2
set2.symmetric_difference(set2)

# 子集
set1 < set2
set1.issubset(set2)

# 真子集
set1 <= set2
set1.issuperset(set2)

print(set1)
print(set2)
