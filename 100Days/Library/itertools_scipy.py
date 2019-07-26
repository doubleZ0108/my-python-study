import itertools
from scipy.special import perm, comb

# 排列
## A(4,2)的数值
print(perm(4,2))

## A(4,2)的所有可能情况
for item in itertools.permutations('ABCD', 2):
        print(item)
c
## 全排列
for item in itertools.permutations('ABCD'):
        print(item)


# 组合
## C(5,3)的数值
print(comb(5,3))
## C(5,3)的所有可能情况
for item in itertools.combinations('ABCDE', 3):
        print(item)


# 笛卡尔积
for item in itertools.product('ABCD', '123'):
        print(item)
