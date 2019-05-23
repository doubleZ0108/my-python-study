## 字符串
str = 'hello world'

# 字符串长度
len(str)
# 获得首字母大写的拷贝
str.capitalize()
#获得全变成大写的拷贝
str.upper()

# 查找子串
str.find('or')		# => 8
str.find('shift')	# => -1

# 字符串是否以指定字符串开头/结尾
str.startswith('He')	# => False
str.endswith('!')	# => True

# 填充字符5"串
str.center(50, '*')	# 将字符串以指定的宽度居中并在两侧填充指定的字符
str.rjust(50,' ')		# 左侧填补空格使总长度为50

# 修建左右两侧空格
str.strip()

# 切片
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45
