'''
for执行完毕会执行执行else
即使有if
除非for中有break直接跳到循环外部
'''
for i in range(3):
    print(i)
else:
    print(i, 'else')    # 当i==2时跳到这条语句执行


# 这里else跟for配对, 而不是if
for i in range(10):
    if i%2:
        print(i)
else:
    print(i, 'else')

# 这里就不会执行else语句
for i in range(10):
    print(i)
    if i==6:
        break
else:
    print(i, 'else')