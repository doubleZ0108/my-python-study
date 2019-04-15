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


str='doubleZ'
print(str[0])
print(str[1:4])	#截取长度 [start_index:end_index+1]     所以输出的好似1，2，3位的字符
print(str[-1])	#输出最后一个字符 Z

num=1
str='3'
sum=num+int(str)	#将string类型转化为int之后就可正常相加了
print('sum is ',sum)


#列表
#列表是任意对象的有序集合
list = ["Python",12,[0,1,2],3,14,True]
print(list)
print("The third elem of list is ",list[2])

list.remove(12)	#删除某个元素（不是某个位置
print(list)


#元组 tuple
#元组的元素不能修改
tuple = ['abc',76,'zz',5.2]
print(tuple[1:3])

#集合 set
#无序不重复元素的序列
age = set([18,19,18,20,21,20])
# age = {18,19,18,20,21,20}, 如果是空集则必须用set函数创建
print(age)

#字典
#无序的key-value对
information ={
	'name':'double Z',
	'age':'18'
}
print(information)

information['sex']='boy'	#在字典中增加数据
del information['age']	#删除数据
print(information)



#语句和函数
#条件语句
password = input()
if password == '12345':
	print('user login success')
elif password == '00000':
	print('administor login success')
else:
	print('wrong password')
	
	
#循环
sum = 0
for i in range(1,10,1):		#第三个参数为每次的增量， 这里i从1～9
	sum = sum + i
print(sum)

#如果是列表或者字典，就不用range函数
list = list([1,'zz',3.14,999])
for i in list:
	print(i)
