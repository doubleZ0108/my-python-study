'''
[1~100000000求和](只为测试单进程/多进程的性能区别)
'''
from time import time
from multiprocessing import Process, Queue

def Single_Process(number_list):
    total = 0
    start = time()
    for num in number_list:
        total += num
    print(total)
    end = time()
    print('Single_Process Execute Time: %.2f' % (end - start))


'''
忽略切片操作花费的时间
只统计做运算和合并运算结果的时间
'''
def tackHandeler(curr_list, result_queue):
    total = 0
    for num in curr_list:
        total += num
    result_queue.put(total)

def Multi_Process(number_list):
    processes = []
    result_queue = Queue()
    index = 0
    # 启动8个进程, 每个进程计算一部分
    for _ in range(8):
        p = Process(target=tackHandeler, args=(number_list[index:index+12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()

    start = time()
    for process in processes:
        process.join()

    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Multi_Process Execute Time: %.2f' % (end - start))



if __name__ == "__main__":
    number_list = [x for x in range(1,100000001)]

    Single_Process(number_list)
    Multi_Process(number_list)
