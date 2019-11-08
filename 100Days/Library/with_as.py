'''
with - as
适合事前需要准备, 事后需要处理的任务

例如. 文件操作需要先打开文件, 操作完再关闭文件
'''

fp = open(r'url...', 'r')
try:
    contents = fp.readlines()
finally:
    fp.close()

# <=>

with open(r'url...') as fp:
    contents = fp.readlines()