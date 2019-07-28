from time import sleep
import threading
from concurrent.futures import ThreadPoolExecutor

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    @property
    def balance(self):
        return self._balance

    def deposit(self, money):
        with self._lock:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance

class AddMoneyThread(threading.Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.desposit(money)

def main():
    account = Account()

    # 创建线程池
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []

    for _ in range(100):
        # 直接启动线程
        # threading.Thread(target=account.deposit, args=(1,)).start()
        
        # 使用线程类
        # AddMoneyThread(account,1).start()
        
        # 使用线程池
        future = pool.submit(account.deposit,1)
        futures.append(future)

    # 关闭线程池
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)

if __name__ == "__main__":
    main()
