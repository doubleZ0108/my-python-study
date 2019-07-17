import sys
# 数据结构
## 列表
list1 = [1,2,5,10,100]
len(list1)
list1.append(200)       # 在列表后追加
list1.insert(1,999)     # 在下标1之前添加
list1 += [88,88]
list1.remove(88)        # 删除第一个出现的88
# list1.remove(10086)   # 引发异常
del list1[0]            # 删除第一个元素

### 复制列表
list2 = list1           # 没有复制列表，只是创建了新的引用
list3 = list1[:]        # 通过完整切片复制列表
list4 = list1[::-1]     # 倒转列表

# ### 排序
sorted_list = sorted(list1) # 返回排序后的拷贝，不会修改原列表
rev_sorted_list = sorted(list1, reverse=True)   # 逆序排序
len_sorted_list = sorted(list1, key=len)        # 对字符串按照长度排序而不是字典序

list1.sort()    # 对列表本身排序

## 列表生成语法
f = [x for x in range(1,11)]
print(f)
f = [x+y for x in 'ABCDE' for y in '1234567']
print(f)
