'''
目标方程：
    z = -x1 + 4x2
约束条件:
    -3x1 + x2 <= 6
    1x1 + 2x2 <= 4
    x2 >= -3


如果是求最大值 <=> -z = x1 - 4x2 的最小值
即修改为 destc = [1,-4]
'''

from scipy.optimize import linprog

destc = [-1,4]      # 目标方程的系数
# 求最大值的时候替换为 destc = [1,-4]

constraintC = [     # 约束方程的系数矩阵
    [-3,1],
    [1,2]
]
constraintB = [6,4] # 约束方程的右端值

x1_bound = [None,None]
x2_bound = [-3,None]

res = linprog(destc,constraintC,constraintB,bounds=(x1_bound,x2_bound))
    #默认求解的是 最小值min

print(res)
print(res.fun)      # 最优解
print(res.x)        # 取到最优值的点
