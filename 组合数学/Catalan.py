from sympy import *

print("你想输出卡特兰数多少位")
MaxSize = input()

for i in range(int(MaxSize)):
	print(catalan(i))
