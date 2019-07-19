# 正则表达式

# compile -> 编译正则表达式, 返回正则表达式对象
# findall -> 查找字符串所有域正则表达式匹配的模式, 返回字符串的列表
# finditer -> 查找字符串所有域正则表达式匹配的模式, 返回迭代器
# search -> 搜索字符串中第一次出现正则表达式的模式, 成功返回匹配对象, 失败返回None

import re

def RE_findall(pattern, sentence):
    mylist = re.findall(pattern, sentence)
    print(mylist)   # list

def RE_finditer(pattern, sentence):
    for temp in pattern.finditer(sentence):
        print(temp.group())  # str


def RE_search(pattern, sentence):
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

if __name__ == "__main__":
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    我的手机号码是13898302345(显然是乱写的), 还有可能是15134850238,
    当然也可能是15248486713, 或者如果我说是18932348651也是极有可能的
    '''

    # RE_findall(pattern, sentence)
    # RE_finditer(pattern, sentence)
    # RE_search(pattern, sentence)
