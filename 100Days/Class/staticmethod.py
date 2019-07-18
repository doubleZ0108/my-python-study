from math import sqrt
# 静态方法
class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 在创建三角形对象之前应该先判断三边是否合法
    # 在这个时候对象还没创建出来, 所以不能调用对象方法
    @staticmethod
    def is_valid(a, b, c):
        return a+b>c and b+c>a and a+c>b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

if __name__=="__main__":

    a,b,c = 3,4,5
    
    if Triangle.is_valid(a,b,c):        # 调用静态方法
        t = Triangle(a,b,c)
        print(t.perimeter())
        print(t.area())
