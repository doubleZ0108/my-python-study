# 类之间的关系

from abc import ABCMeta, abstractclassmethod

# 抽象类
class Person (object, metaclass=ABCMeta):
	def __init__(self,name,age):
		self._name = name
		self._age = age
		
	@property
	def name(self):
		return self._name
		
	@property
	def age(self):
		return self._age
		
	@age.setter
	def age(self,age):
		self._age = age
		
	# 抽象方法（需要实例化）
	@abstractclassmethod
	def display(self):
		pass
		
		
		
class Student(Person):
	def __init__(self,name,age,grade):
		super().__init__(name,age)
		self._grade = grade
		
	@property
	def grade(self):
		return self._grade
		
	@grade.setter
	def grade(self,grade):
		self._grade = grade
		
	def display(self):
		print('Student: name is %s, age is %d, grade = %f' % (self._name,self._age,self._grade))
		

def main():
	# p = Person('一个人',18)
	# p.display()
	s = Student('zz',19,99.99)
	s.display()
	
	
if __name__ == '__main__':
	main()
