from PIL import Image, ImageFilter

img = Image.open('Resources/img.jpg')

# 显示图像
img.show()

# 裁剪
rect = 80, 20, 310, 360
img.crop(rect).show()

# 旋转
img.rotate(180).show()

# 翻转
img.transpose(Image.FLIP_LEFT_RIGHT).show()

# 生成缩略图
size = 128,128
img.thumbnail(size)
img.show()

# 缩放
width,height = img.size
img = img.resize((int(width*0.3),int(height*0.3)))
img.show()

# 粘帖图象
img2 = Image.open('Resources/her.jpg')
img2.paste(img,(100,200))   # 第二个参数为位置
img2.show()

# 操作像素
for x in range(280,450):
    for y in range(100,350):
        img.putpixel((x,y),(255,0,0))
img.show()

# 滤镜
img.filter(ImageFilter.CONTOUR).show()
