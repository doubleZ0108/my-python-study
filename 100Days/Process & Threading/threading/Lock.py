'''
[模拟100个线程向同一个账户转账(1元)]

结果: 账户中远远小于100元(1~2元)

原因: 一个资源被多个线程竞争使用, 会得到错误结果
      多个线程同时向账户中存钱, 同时执行到 new_balance = self._balance + money
      多个线程的初始账户余额都是0, 大家都是在0的基础上加了1元钱

解决方案: 通过"锁"来保护"临界资源"
         只有获得锁的线程才能访问临界资源
         其他没有得到锁的线程被阻塞起来, 直到获得锁的进程释放了锁
'''

from time import sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先要获取锁才能执行后续代码
        self._lock.acquire()

        try:
            new_balance = self._balance + money
            sleep(0.01)     # 模拟受理存款业务需要0.01秒时间
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作, 保证正常异常, 锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

if __name__ == "__main__":

    account = Account()     # 创建一个银行账户

    threads = []
    for _ in range(100):    # 创建100个线程并启动
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    
    for t in threads:       # 等待所有存款线程都执行完毕
        t.join()

    print('账户余额为: %d元' % account.balance)
