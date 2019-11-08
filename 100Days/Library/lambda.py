ans = (lambda x,y: x*y)(3,4)
print(ans)

arr = [{'name':'doubleZ', 'age':19}, {'name':'yt', 'age':18}, {'name':'fff', 'age':1}]
# 按姓名排序
arr = sorted(arr, key=lambda x:x['name'])
print(arr)
# 按年龄排序
arr = sorted(arr, key=lambda x:x['age'])
print(arr)