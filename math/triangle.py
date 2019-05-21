
import math

# 海伦公式：用三角形三边长计算面积
a = input('please input a = ')
b = input('please input b = ')
c = input('please input c = ')
if a+b>c and a+c>b and b+c>a:
	p = (a+b+c)/2
	area = math.sqrt(p * (p - a) * (p - b) * (p - c))
	print("面积为： %f" % (area))
else:
	print("不能构成三角形")
