## 字典
scores = {'zz':100, 'yt':99, 'gf':60}

# 通过键获取字典中对应的值
print(scores['zz'])
print(scores.get('zz'))	# 可以设置默认值
print(scores.get('aa',999))	# 如果字典中没有该元素就会返回默认值

# 遍历字典
for elem in scores:
	print('%s --> %d' % (elem,scores[elem]))
	
# 更新字典元素
scores['sm'] = 58
scores.update(gp=2,ly=3)
print(scores)

# 删除元素
print(scores.popitem())
print(scores)
print(scores.pop('gp'))
print(scores)
