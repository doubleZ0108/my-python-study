# 正则表达式

# split -> 用正则表达式指定的模式分隔符踹分字符串, 返回列表

import re

def RE_split(pattern, poem):
    sentence_list = re.split(pattern, poem)
    while '' in sentence_list:
        sentence_list.remove('')
    return sentence_list

if __name__ == '__main__':
    pattern = r'[，。, .]'
    poem = '床前明月光, 疑是地上霜。 举头望明月, 低头思故乡。'
    print(RE_split(pattern, poem))
