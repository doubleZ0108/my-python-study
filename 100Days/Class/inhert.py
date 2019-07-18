class People(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
    
    def display(self):
        print('%d岁数的%s正在玩' % (self._age, self._name))

class Student(People):
    def __init__(self, name, age, score):
        super().__init__(name, age)     # 先调用父类的构造函数
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self):
        self._score = score

    def stu_display(self):
        print('%d岁数的%s的分数是%f' % (self._age, self._name, self._score))


if __name__ == "__main__":
    stu = Student('zz', 19, 99.5)
    stu.display();
    stu.age = 200
    stu.stu_display()
    print(stu.score)
