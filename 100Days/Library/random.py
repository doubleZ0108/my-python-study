from random import randint, uniform
# 随机整数
randint(1,10)

# 随机浮点数
uniform(1.5,10.5)


import numpy as np
# 正态分布随机数
li = np.random.normal(mu, sigma, num)   # 返回的是num个正态分布随机数列表，即使只产生一个数引用的时候也要写li[0]
