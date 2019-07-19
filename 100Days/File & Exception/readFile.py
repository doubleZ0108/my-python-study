# 文件与异常
## 读取文件

'''
一次性读取整个文件
'''
def readFile_whole():
    with open('this.txt', 'r', encoding='utf-8') as f:
        print(f.read())


'''
逐行读取
'''
def readFile_lineByline():
    with open('this.txt', mode='r') as f:
        for line in f:
            print(line, end='')


'''
按行读取到列表中
'''
def readFile_lines():
    with open('this.txt') as f:
        lines = f.readlines()

    for line in lines:
        print(line, end='')


if __name__ == "__main__":
    readFile_whole()
    readFile_lineByline()
    readFile_lines()
