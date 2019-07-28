'''
多进程和进程池

多线程因为GIL的存在不能够发挥CPU的多核特性
对于计算密集型任务应该考虑用多进程
'''

import concurrent.futures
import math
from time import time

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    if n%2==0:
        return False
    for i in range(3, int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def Multi_Process():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES,executor.map(is_prime,PRIMES)):
            print('%d is prime: %s' % (number,prime))

def Single_Process():
    for prime in PRIMES:
        print('%d is prime: %s' % (prime, is_prime(prime)))


if __name__ == "__main__":
    start = time()
    Multi_Process()
    end = time()
    print('Multi_Process: ', end-start)     # 3.907235860824585

    start = time()
    Single_Process()
    end = time()
    print('Single_Process: ', end-start)    # 13.447319984436035


