'''
并发编程 (Concurrent Programming)
1.提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2.改善用户体验 - 让耗时间的操作不会造成程序的假死
'''

# 将文件夹中的所有.png图片转换为三种格式的缩略图并存储到指定目录下
import glob
import os
import threading
from PIL import Image

TARGET_PATH = 'thunbnails'

def generate_thumbnail(infile, size, format='PNG'):
    path,file = os.path.split(infile)    # 将路径和文件名分开  Resources/Img tent.png
    filename = file[:file.rfind('.')]     # 获取文件名
    ext = file[file.rfind('.')+1:]
    outfile = f'{TARGET_PATH}/{filename}_{size[0]}_{size[1]}.{ext}'
    img = Image.open(infile)
    img.thumbnail(size, Image.ANTIALIAS)
    img.save(outfile, format)

def main():
    if not os.path.exists(TARGET_PATH):
        os.mkdir(TARGET_PATH)
    for infile in glob.glob('Resources/Img/*.png'):     # 所有的.png文件
        for size in (32,64,128):
            threading.Thread(target=generate_thumbnail,args=(infile,(size,size))).start()

if __name__ == "__main__":
    main()
