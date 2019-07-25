from random import randint
import numpy as np
# 语法🍬
## 列表生成式
'''
L = [exp for iter_var in iterable if_exp]
<=>
L = []
for iter_var in iterable:
    if if_exp:
        L.append(exp)

L = [exp for iter_var_A in iterable_A for iter_var_B in iterable_B]
<=>
L = []
for iter_var_A in iterable_A:
    for iter_var_B in iterable_B:
        L.append(exp)
'''
### 生成平方序列
list1 = [x**2 for x in range(1,10)]
print(list1)

### 生成字母序列
list2 = [chr(ord('A')+x) for x in range(0,3)]  # ord():把单字符转化为整数，chr():把整数转化为Unicode字符
print(list2)

### 过滤列表
list3 = np.random.randint(0,100,20)
list3 = [x for x in list3 if not x%2]   # 过滤掉奇数
print(list3)

### 生成全排列
l1 = [x for x in range(1,5)]
l2 = [chr(ord('A')+x) for x in range(0,3)]
list4 = [(x,y) for x in l1 for y in l2]
print(list4)


grade_dict = {
    'zz':100,
    'yT':99,
    'gf':70,
    'sm':57,
    'gp':60,
}
### 将字典转换成元祖组成的列表
list5 = [(key,value) for key,value in grade_dict.items()]
print(list5)

## 字典生成语法
upper_grade_dict = {key:value for key,value in grade_dict.items() if value>60}
print(upper_grade_dict)

## 集合生成语法
set1 = {1,1,2,2,2,3,4,5,5,6}
set1 = {x for x in set1 if x%2}
print(set1)
