from random import sample

## sample -> 从列表中选择不重复的n个元素
nums = [x for x in range(1,11)]
for i in range(6):
    selected_num = sample(nums, 3)
    print(selected_num)


