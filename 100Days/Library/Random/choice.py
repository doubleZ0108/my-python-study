'''
choice --- 随机选择
迷宫
'''

from random import choice

for i in range(10):
    for j in range(20):
        print(choice('\u2571\u2572'), end='')
    print()
