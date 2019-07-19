## 读取二进制文件
### 复制图片
def copyImg():
    try:
        with open('this.jpg', 'rb') as in_file:
            data = in_file.read()
        with open('copy.jpg', 'wb') as out_file:
            out_file.write(data)
    except FileNotFoundError:
        print('指定的文件无法打开')
    except IOError:
        print('读写文件时发生错误')
    
    print('DONE!')

if __name__ == "__main__":
    copyImg()
