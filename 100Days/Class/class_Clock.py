import time
import os

class myClock(object):
    def __init__(self, hour=0, minute=0, second=0):
        '''初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        '''
        self._hour = hour
        self._minute = minute
        self._second = second

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

if __name__ == "__main__":
    clock = myClock(23,50,55)
    while(True):
        os.system('cls')
        print(clock)        # 调用的时__str__方法
        time.sleep(0.01)
        clock.run()
            
