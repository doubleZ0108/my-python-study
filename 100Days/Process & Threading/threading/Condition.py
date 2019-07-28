'''
多个线程竞争一个资源 -- 锁(Lock)
多个线程竞争多个资源 -- 信号量(Semaphore)
多个线程的调度(暂停线程/唤醒等待的线程) -- Condition
'''

# 启动5个线程向账户中存钱, 5个线程从账户中取钱, 取钱时如果余额不足要暂停线程等待
from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep
import threading

class Account(object):
    def __init__(self, balance=0):
        self._balance = balance
        lock = threading.Lock()
        self._condition = threading.Condition(lock)

    @property
    def balance(self):
        return self._balance

    def withdraw(self, money):
        with self._condition:
            while money>self._balance:
                self._condition.wait()      # 余额不足时, 取钱的线程暂停并释放锁
            new_balance = self._balance - money
            sleep(0.01)
            self._balance = new_balance

    def deposit(self,money):
        with self._condition:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance

def add_money(account):
    while True:
        money = randint(5,10)
        account.deposit(money)
        print(threading.current_thread().name," ===> ",account.balance)
        sleep(0.5)

def sub_money(account):
    while True:
        money = randint(10,30)
        account.withdraw(money)
        print(threading.current_thread().name, ' <=== ',account.balance)
        sleep(1)

if __name__ == "__main__":
    account = Account()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money,account)
            pool.submit(sub_money,account)
