# 装饰器
class Person(object):

    '''
    限定Person对象只能绑定如下三个属性
    __slots__魔法只对当前类的对象盛晓晓, 对子类不起作用
    '''
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器
    @age.setter
    def age(self, age):
        self._age = age
    
    def display(self):
        print('%s今年%d岁了' % (self._name, self._age))

if __name__ == '__main__':
    p = Person('double Z', 19)
    print(p.age, p.name)
    p.display()
    p.age = 99
    p.display()
    # p.name = 'Kerr'   # AttributeError: name没设置修改器
    p._gender = 'male'
    # p._sex = 'b'      # AttributeErrlr: Person对象没有这个属性

