## 元组，元组的元素不能修改
# 元组在多线程环境下更安全也更易维护
# 如果方法要返回多个值，使用元组也是个很不错的选择
# 元组在创建时间和占用的空间傻姑娘都优于列表
t = ('zz',19,True,'Tonghua')

# t[0]='yT'  # 重新给元组赋值将引起TypeError

t = ('yT',19,False,'Taiyuan')	# 变量t重新引用了新的元组，原来的元组将被垃圾回收

# 将元组转换成列表
l = list(t)
l[3]='tongji'	# 列表中的元素是可以修改的

# 将列表转换为元组
fresht = tuple(l)
