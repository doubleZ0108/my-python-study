# 正则表达式

#  match: 用正则表达式匹配字符串
#   成功返回匹配对象
#   否则返回None

"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：
    用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
    QQ号是5~12的数字且首位不能为0
"""
import re

def usernameCheck(username):
    m = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m:
        print('请输入正确的用户名')
        return False
    else:
        return True

def qqCheck(qq):
    m = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m:
        print('请输入有效的qq号')    
        return False
    else:
        return True

if __name__ == "__main__":
    username = input('请输入用户名: ')
    qq = input('请输入qq号: ')

    if usernameCheck(username) and qqCheck(qq):
        print('输入的是有效的信息!')
