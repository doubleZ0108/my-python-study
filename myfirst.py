#单行注释
'''
多行注释1
多行注释2
多行注释3
'''

#用户输入函数
print("请输入你的名字")
name=input()
print("你的名字是",name)

#查看python保留字
import keyword
print(keyword.kwlist)

#查看变量数据类型
a=1
b=3.16 
c=True 
print(type(a))
print(type(b))
print(type(c))

#代数运算
print(15/4)		#输出3.75
print(15//4)	#整除运算：输出3
print(2**3)		#乘方运算：输出8

#字符串
##单引号包裹
print('What\'s your name?')	#单引号要加转义字符\
##双引号包裹
print("What's your name?")	#单引号可以自由使用
###三引号包裹：可以表示多行字符串 （可以自由使用单双引号）
print('''the first line
the second line
the third line''')

#在print字符串开始的部分加上r, 怎整个语句不会进行转义字符理解
print(r'this is a string that would not deal with \n')  #输出: this is a string that would not deal with \n
