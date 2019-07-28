'''
赋值: 可以理解为 li is assign_li and li[i] is assign_li[i]
     由于二者指向同一对象, 对li的任何修改都会体现在assign_li上

浅拷贝:  只拷贝父对象, 不会拷贝对象内部的子对象
    · 切片[:]操作
    · 工厂函数(list/dir/set等)
    · copy.copy()函数
深拷贝:  拷贝对象及其子对象
    · 如果元组容齐只包含原子类型对象, 则不能深拷贝
    li = (1,2,'python',1.234,'tongji')
    deepcopy_li = copy.deepcopy(li)
    print(li is deepcopy_li)    # True

注: 对于非容器类型(数字, 字符串等)没有拷贝这一说
    obj is copy.copy(obj) and obj is copy.deepcopy(obj)
'''
import copy
li = [1, 2, 3, 4, ['a', 'b']]  #原始对象

assign_li = li                   #赋值，传对象的引用
copy_li = copy.copy(li)        #对象拷贝，浅拷贝
deepcopy_li = copy.deepcopy(li)    #对象拷贝，深拷贝

li.append(5)  #修改对象a
li[4].append('c')  #修改对象a中的['a', 'b']数组对象

print(li)    # [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print(assign_li)    # [1, 2, 3, 4, ['a', 'b', 'c'], 5]  就是a
print(copy_li)    # [1, 2, 3, 4, ['a', 'b', 'c']]     更改父对象不会改变原对象, 改变子对象依然会作用与原对象的子对象
print(deepcopy_li)    # [1, 2, 3, 4, ['a', 'b']]
