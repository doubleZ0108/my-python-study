# enumerate -> 既遍历出数值又遍历出索引
li = [54,12,6,8,5,23,1]
for index,item in enumerate(li):
    print(index, item)


names = ['zz','yt','gf','sm','ly']
courses = ['语文','数学','英语']
scores = [[None]*len(courses) for _ in range(len(names))]
for row,name in enumerate(names):
    for col,course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}课成绩'))
