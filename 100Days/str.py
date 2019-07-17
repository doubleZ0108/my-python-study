str1 = "hello world\n"
len(str1)               # 获取长度
str1.capitalize()       # 首字母大写的拷贝 -> Hello world
str1.upper()            # 所有字母大写 -> HELLO WORLD

# 查找子串
print(str1.find('or'))
str1.find('or')     # 7
str1.find('shit')   # -1
# str1.index('or'); # 找不到子串时会引发异常

str1.startswith('hel')  # 是否以指定字符串开头 -> True
str1.endswith('LD')     # False


# 下标运算
str2 = "abc123456"
str2[2:5]   # c12
str2[2:]    # c123456
str2[2::2]  # c246
str2[::-1]  # 654321cba
str2[-3:-1] #45

str2.isdigit()  # 字符串是否由数字构成 -> False
str2.isalpha()  # 字符串是否由字母构成 -> False
str2.isalnum()  # 字符串是否由数字和字母构成 -> True

str3 = "    doubleZ0108@163.com "
str3.strip()    # 去除左右两侧的指定字符 -> 默认是空格
