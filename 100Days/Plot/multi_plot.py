# -*- coding: UTF-8 -*-
'''
一个折线图绘制多个曲线
'''
import matplotlib.pyplot as plt
from random import randint
 
# 数据
x_axix = [_ for _ in range(10)]
y1_axix = list(map(lambda x:randint(0, 100), [_ for _ in range(10)]))
y2_axix = list(map(lambda x:randint(0, 100), [_ for _ in range(10)]))
y3_axix = list(map(lambda x:randint(0, 100), [_ for _ in range(10)]))
#开始画图

plt.title('Result Analysis')
plt.plot(x_axix, y1_axix, color='red', label='testing accuracy')
plt.plot(x_axix, y2_axix, color='skyblue', label='PN distance')
plt.plot(x_axix, y3_axix, color='blue', label='threshold')

plt.legend() # 显示图例

plt.xlabel('x label name')
plt.ylabel('y label name')
plt.show()
