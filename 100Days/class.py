class Student(object):
    def __init__(self, name, age, buf):
        self.name = name
        self.age = age
        self.__buf = buf    # 两个下划线是私有对象

    def study(self, course_name):
        print('%d的%s正在学习%s' % (self.age, self.name, course_name))

    def __foo(self):        # 两个下划线是私有方法, 外界不可以访问
        print(self.__buf)

if __name__=="__main__":
    s1 = Student('double Z', 19, 'hello')
    s1.study('Python程序设计')
    print(s1.name)
