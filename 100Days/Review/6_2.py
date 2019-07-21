from multiprocessing import Process,Lock
from time import time, sleep
from os import getpid
from random import randint
from threading import Thread

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

class AddmoneyHandler(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


if __name__ == "__main__":
    account = Account()
    threadings = []
    for _ in range(100):
        t = AddmoneyHandler(account, 1)
        threadings.append(t)
        t.start()

    for threading in threadings:
        threading.join()

    print(account.balance)
    
