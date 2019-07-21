





# Python多进程_复杂任务分而治之问题

[TOC]

## 问题描述

求解1~1000000求和的计算密集型任务

## 多进程求解方法

- 首先将所有待求和数字加入列表`l`中
- 创建`processNum`个进程, 每个进程求解一个列表切片的和, 并将其加入队列
- 最终将所有进程的切片和累加起来得到所有数字的和

## 代码实现

初始化待求和列表

```python
l = [x for x in range(1,1000001)]
```

创建多个进程, 每个进程求解一个列表切片的值

```python
for _ in range(processNum):
    p = Process(target=SumHandler, args=(l[index:index+1000000//processNum], result_queue))
    index += 1000000//processNum
    processes.append(p)
    p.start()
```

单个进程求解逻辑

```python
def SumHandler(curr_list, result_queue):
    total = 0
    for num in curr_list:
        total += num
    result_queue.put(total)
```

等待所有进程执行完毕

```python
for process in processes:
    process.join()
```

合并所有切片的和得到问题最终的解

```python
while not result_queue.empty():
    total += result_queue.get()
print(total)
```

## 实验步骤

1. 依次使用`1`~`Total_processNum`个进程对问题进行求解

2. 每次求解时记录该问题规模和进程数量情况下的执行时间:

   - 第一种计时方式只考虑**所有进程的计算时间**和**合并最终结果的时间**

     ```python
     # 进程创建 & 列表切片
     
     start = time()
     
     # 所有进程的进行运算
     # 合并最终结果
     
     end = time()
     ```
   - 第二种计时方式将**进程创建时间**和**切片时间**考虑在内

     ```python
     start = time()
     
     # 进程创建 & 列表切片
     # 所有进程的进行运算
     # 合并最终结果
     
     end = time()
     ```
   
3. 最终以*进程数量*为<u>横坐标</u>, *运行时间*为<u>纵坐标</u>分别绘制**多进程-执行时间图像**

## 实验结果

### Windows系统

只考虑**所有进程的计算时间**和**合并最终结果的时间**

![Windows_不计算创建进程时间.png](https://upload-images.jianshu.io/upload_images/12014150-8e8240e83f9ce72e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

将**进程创建时间**和**切片时间**考虑在内

![Windows_计算创建进程时间.png](https://upload-images.jianshu.io/upload_images/12014150-ec444e40c2c74ac7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### MacOS系统

只考虑**所有进程的计算时间**和**合并最终结果的时间**

![MacOS_不计算创建进程时间.jpg](https://upload-images.jianshu.io/upload_images/12014150-d4d4d27c26f1c5b6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

将**进程创建时间**和**切片时间**考虑在内

![MacOS_计算创建进程时间.jpg](https://upload-images.jianshu.io/upload_images/12014150-b769eba10f38b1be.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 结果分析

### 两种计时方式结果的差别

- 只考虑**所有进程的计算时间**和**合并最终结果的时间**: 随着使用的计算进程数量的增多, 问题的求解时间逐渐减少, 且随着进程数量趋于无限大(小于数字总数), 运行时间逐渐趋于某个最小执行时间
- 将**进程创建时间**和**切片时间**考虑在内: 随着使用的计算进程数量的增多, 问题的求解时间逐渐增多, 且图像近似满足一次函数
- 第一种计时方式大致满足我们的直观感受, 刚开始进程数量的增多, 运行速度提升的幅度很大, 多个进程同时进行运算的效果很好, 随着进程数量的进一步增多, 每个进程所分配到的切片长度很短, 函数调用等时间会弱化多进程同时执行得到的效果, 同时合并时间也增加, 因此最终趋于一个最少的运行时间下界
- 第二种计时方式的结果应该是由于创建进程的时间随进程数增多而线性增加, 而相较于计算简单的加法运算而言, 创建进程的时间要大的多, 因此多进程同时进行运算的优势被创建进程花费的时间掩盖掉
- **问题在于我们使用多进程就是希望能提高运行速度, 减小运行时间, 所以应该综合的考虑所有时间, 按照现在的实验效果来讲多进程的实验效果并不理想**

### Windows系统和MacOS系统运行结果的差别

从图像中我们可以发现MacOS系统运行的结果中在进程数为40~60的区间段内运行时间都明显增加, 且幅度很巨大, 不知道是MacOS系统设定的限定还是其他什么原因?



## 进一步拓展

将多进程改用**多线程**

```python
from threading import Thread
...
t = Thread(target=SumHandler, args=(l[index:index+1000000//processNum], result_queue))
...
```

### 运行结果

#### Windows系统

只考虑**所有进程的计算时间**和**合并最终结果的时间**

![Windows_只考虑.png](https://upload-images.jianshu.io/upload_images/12014150-953e85e27e139a94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

将**进程创建时间**和**切片时间**考虑在内

![Windows_都考虑.png](https://upload-images.jianshu.io/upload_images/12014150-789628c18b380d3e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

#### MacOS系统

只考虑**所有进程的计算时间**和**合并最终结果的时间**

![MacOS_只考虑.jpg](https://upload-images.jianshu.io/upload_images/12014150-53c98aa4b63723a3.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

将**进程创建时间**和**切片时间**考虑在内

![MacOS_都考虑.jpg](https://upload-images.jianshu.io/upload_images/12014150-161b797660d8d1e9.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 结果分析

改用线程后运行速度明显提高了一个档次, 跑大数据量时速度很快

但是问题就更多了

1. 只考虑**所有进程的计算时间**和**合并最终结果的时间**时实验结果跟之前进程的大体相同, 但是在MacOS系统上运行时函数一阶导从0到无穷大, 二阶导小于零, 凸函数; 而Windows上是一阶导从负无穷大到0, 二阶导大于零, 凹函数

   不知道两个操作系统为什么运行结果有这个大的差距

2. 将**进程创建时间**和**切片时间**考虑在内时不太能直观的看出来运行时间和线程数量的关系, 大致只能描述为运行时间与进程数量关系不大?

## 又进一步扩展(不死心)

在使用多线程的基础上讲最大线程总数提高一个数量级, 最多线程为1000个

### 运行结果

#### Windows系统

只考虑**所有进程的计算时间**和**合并最终结果的时间**

![image.png](https://upload-images.jianshu.io/upload_images/12014150-a0698e6df2a5dcbd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

将**进程创建时间**和**切片时间**考虑在内

![进程数1000.png](https://upload-images.jianshu.io/upload_images/12014150-9a41650eb2040893.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 结果分析

1. 只考虑**所有进程的计算时间**和**合并最终结果的时间**时, 在100之前确实时降低, 但是100~1000是开始逐渐增加, 并且增加的不是很有规律性, 散点分布在一个条带区间内(不太懂为什么)
2. 将**进程创建时间**和**切片时间**考虑在内时, 趋势仍是递增, 但是散点也是分布在一个条带内(机器执行的结果人真的是没法猜测)