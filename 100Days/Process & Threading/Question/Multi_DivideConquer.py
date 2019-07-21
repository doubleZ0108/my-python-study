from multiprocessing import Process, Queue
from threading import Thread
from time import time
import matplotlib.pyplot as plt

def SumHandler(curr_list, result_queue):
    total = 0
    for num in curr_list:
        total += num
    result_queue.put(total)

if __name__ == "__main__":
    Total_processNum = 1000
    time_list = []
    l = [x for x in range(1,1000001)]

    for processNum in range(1,Total_processNum+1):
        # print('使用%d个进程' % processNum)
        processes = []
        result_queue = Queue()
        index = 0
        total = 0

        # start = time()

        for _ in range(processNum):
            p = Process(target=SumHandler, args=(l[index:index+1000000//processNum], result_queue))
            index += 1000000//processNum
            processes.append(p)
            p.start()
        
        start = time()

        for process in processes:
            process.join()

        while not result_queue.empty():
            total += result_queue.get()

        end = time()
        # print(total)
        # print('总耗时%.2f' % (end-start))
        time_list.append(end-start)

    
    plt.plot([x for x in range(1,Total_processNum+1)], time_list, 'ro')
    plt.xlabel("Data Amount")
    plt.ylabel("Execute Time")
    plt.show()
