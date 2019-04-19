#创建类
class myClass:
    def __init__(self, name, age):  #构造函数
        self.name = name
        self.age = age

    def hello(self, newname):  #self是必须写的, 其他是传递的参数
        self.name = newname
        print('hello ', self.name)

    def say(self):
        print('say a word')


obj = myClass('double Z', 18)

obj.say()           #调用的时候实际相当于obj.say(obj), 把自己作为参数传递给self
obj.hello('Kerr')
