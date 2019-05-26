from time import time,localtime,sleep

class Student (object):
	
	# 限定Student对像智能绑定这三个属性（可以动态扩充）
	__slots__ = ('_name','_age','_gender')
	
	def __init__(self,name,age):
		# ,self.__foo = 0
		self._name = name	# 为学生对戏那个绑定name和age两个属性
		self._age = age
		
	# 定义私有方法：属性命名时用两个下划线作为开头
	def __bar(self):
		print('这是一个私有属性')
		
		
	# 访问器 - getter方法
	@property
	def name(self):
		return self._name		# 可以读name
	@property
	def age(self):
		return self._age		# 可以读age
		
	# 修改器 - setter方法
	@age.setter
	def age(self,age):
		self._age = age			# 可以写age
		
def StudentMain():
	s = Student('zz',19)
	# s.__bar()		# AttributeError
	# print(s.__foo)
	
	print('%s的年龄时%d' % (s.name,s.age))
	s.age = 20
	# s.name = 'yt'	# 因为卖给name属性setter所以会引发AttributeError
	
	s._gender = 'boy'
	
	
	
	
class Triangle(object):
	def __init__(self,a,b,c):
		self._a = a
		self._b = b
		self._c = c
		
	# 定义静态方法，在对象尚未创建出来就要调用这个方法，它属于类的方法
	@staticmethod
	def is_valid(a,b,c):
		return a+b>c and a+c>b and b+c>a
		
def TriangleMain():
	a,b,c = 3,4,5
	if Triangle.is_valid(a,b,c):
		t = Triangle(a,b,c)	# 实例化对象
	else:
		print('无法构成三角形')
	
	
	
class Clock(object):
	def __init__(self,hour=0,minute=0,second=0):
		self._hour = hour
		self._minute = minute
		self._second = second
		
	# 类方法，cls参数代表当前类相关的信息，通过cls可以获取和类相关的信息并且可以创建出类的对象	
	@classmethod
	def now(cls):
		ctime = localtime(time())
		return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)
		
	def show(self):
		return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)
		
def ClockMain():
	clock = Clock.now()
	print(clock.show())
		
if __name__ == '__main__':
	# StudentMain()
	# TriangleMain()
	ClockMain()
