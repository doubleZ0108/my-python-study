from random import sample

## enumerate -> 既遍历出数值又遍历出索引
li = [54,12,6,8,5,23,1]
for index,item in enumerate(li):
    print(index, item)

## sample -> 从列表中选择不重复的n个元素
nums = [x for x in range(1,11)]
for i in range(6):
    selected_num = sample(nums, 3)
    print(selected_num)


