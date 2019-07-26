# 堆
import heapq

## 找列表中最大/小的几个元素
my_list = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
print(heapq.nlargest(3,my_list))
print(heapq.nsmallest(5,my_list))

## 指定字典的某个key
my_dict = list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(2,my_dict,key=lambda x: x['price']))
print(heapq.nsmallest(3,my_dict,key=lambda x: x['shares']))
