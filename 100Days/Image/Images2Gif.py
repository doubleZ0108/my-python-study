'''
Resources/Result/目录下有多张图片
图片格式: framexx.png
'''
import os
from PIL import Image
import imageio

dirname = 'Resources/Result/'
frames = list(filter(lambda x: x[0:5]=='frame' and x[-4:]=='.png', os.listdir(dirname)))    # 将不符合命名要求的图片过滤掉(MacOS)会默认创建一些文件
frames.sort(key=lambda x: int(x[5:-4]))     # 按照图片编号进行排序

'''
imageio库：效率有点低，合并很多张图片容易卡死
'''
def myImage2Gif_imageio(dirname):
    frames = list(filter(lambda x: x[0:5] == 'frame' and x[-4:] == '.png', os.listdir(dirname)))  # 将不符合命名要求的图片过滤掉(MacOS)会默认创建一些文件
    frames.sort(key=lambda x: int(x[5:-4]))     # 按照图片编号进行排序

    imgs = []
    for frame in frames:
        imgs.append(imageio.imread(dirname+frame))
    imageio.mimsave(dirname+'result.gif', imgs, 'GIF', duration=0.35)

'''
有点莫名其妙，有时候会只在首位两张图片之间闪烁(可能是duration是按毫秒计时，改成300效果很好)
'''
def myImage2Gif_PIL():
    imgs = []
    for frame in frames:
        img = Image.open(dirname+frame)
        imgs.append(img)

    imgs[0].save(dirname + 'result.gif', save_all=True, append_images=imgs, duration=300)
