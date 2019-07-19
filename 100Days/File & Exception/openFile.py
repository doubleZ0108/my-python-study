# 文件和异常
## 读取文件

'''
如过引发异常会导致程序崩溃
'''
def openFile_origin():
    f = open('this.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


'''
捕获异常
finally无论程序正常还是异常都会执行到
'''
def openFile_try():
    try:
        f = open('this.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法代开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解析错误!')
    finally:
        if f:
            f.close()


'''
with指定文件对象的上下文环境
并在离开上下文环境时自动释放文件资源
'''
def openFild_with():
    try:
        with open('this.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法代开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解析错误!')


if __name__ == "__main__":
    openFile_origin()
    openFile_try()
    openFild_with()
