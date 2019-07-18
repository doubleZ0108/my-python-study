from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):       # 使用metaclass和abstractmethod修饰器实现抽象类
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s: 喵喵喵...' % self._nickname)


if __name__=='__main__':
    pets = [Dog('旺财'), Cat('大奶牛'), Dog('球球')]
    for pet in pets:
        pet.make_voice()

    # pet = Pet('这是个名字') # Abstract class 'Pet' with abstract methods instantiated
    # pet.make_voice()    # TypeError: Can't instantiate abstract class Pet with abstract methods make_voice
