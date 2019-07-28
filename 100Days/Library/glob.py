'''
glob -> 查找符合特定规则的文件路径名

"*"匹配0个或多个字符；
"?"匹配单个字符；
"[]"匹配指定范围内的字符，如：[0-9]匹配数字
'''

import glob

# 输出Resources下所有目录中.png图片的文件名
for filename in glob.glob('Resources/*/*.png'):
    print(filename)

# 获取上级目录下所有文件名是一个字符的.py文件 
pyit = glob.iglob('../?.py')    # iglob返回的是迭代器
while True:
    try:
        print(next(pyit))
    except StopIteration:
        break
