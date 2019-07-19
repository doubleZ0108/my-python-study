# 正则表达式

# sub -> 用指定的字符串替换源字符串中与正则表达式匹配的模式
#   count 指定替换的次数
#   flags: re.I / re.IGNORECASE     忽略大小写匹配
#          re.M / re.MULTILINE      多行匹配
import re

def RE_sub(pattern, sentence):
    purified = re.sub(pattern, '*', sentence, count=0, flags=re.IGNORECASE | re.MULTILINE)
    return purified

if __name__ == "__main__":
    pattern = '[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔'
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'

    print(RE_sub(pattern, sentence))
