import os
from time import time, localtime, sleep
# 类方法
class Calendar(object):
    def __init__(self, year, month, date):
        self._year = year
        self._month = month
        self._date = date

    '''
    类方法的第一个参数约定为cls, 代表当前类相关的信息
    通过这个参数可以获取和类相关的信息并可以创建出类

    这个例子里Calendar默认的三个参数是整数
    如果有用户按照 "2000-01-08" 这种字符串的方式输入
    我们就要通过这个类方法提前对参数进行处理
    '''
    @classmethod
    def trans(cls, date_as_string):
        year, month, date = map(int, date_as_string.split('-'))
        return cls(year, month, date)
        
    def show(self):
        print('日期是: %d/%d/%d' % (self._year, self._month, self._month))


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    '''
    先使用类方法获取当前时间
    '''
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        '''走字'''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def __str__(self):
        '''显示时间'''
        return '%2d:%2d:%2d' % (self._hour, self._minute, self._second)

if __name__ == '__main__':
    # cal1 = Calendar.trans("2000-01-08")
    # cal2 = Calendar(2000,2,20)

    # cal1.show()
    # cal2.show()

    cl = Clock.now()
    while True:
        os.system('cls')
        print(cl)
        sleep(0.1)
        cl.run()
