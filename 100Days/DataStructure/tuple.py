# 数据结构
## 元组
'''
1.元组是无法修改的
2.元组在创建时间和占用空间上都优于列表
3.不需要对元素进行增删改，考虑用元组
4.方法要返回多个值，考虑用元组
'''
t = ('double Z', 19, True, "吉林通化")
# t[0] = 'Kerr'   # TypeError
l = list(t)
l[0] = 'Kerr'     # 列表可以修改

new_t = tuple(l)
print(new_t)
