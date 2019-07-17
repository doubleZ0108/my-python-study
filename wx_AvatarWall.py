from wxpy import *
import PIL.Image as Image
import os
import sys

if __name__=="__main__":
    # 初始化机器人，扫码登陆微信
    bot = Bot()
    
    # 在本地创建一个目录用于存储头像
    # 获取当前路径
    curr_dir = get_dir(sys.argv[0])
    if not os.path.exists(curr_dir + "FriendImgs/"):    # 如果FriendImgs目录不存在就创建一个
        os.mkdir(curr_dir + "FriendImgs/")

    # 获取好友头像并存储在本地目录中
    my_friends = bot.friends(update = True)
    n = 0
    for friend in my_friends:
        friend.get_avatar(curr_dir + "FriendImgs/" + str(n) + ".jpg")
        n += 1


    # 生成照片墙
    # 设置照片墙的尺寸
    image = Image.new("RGB", (650,650))
    avatars = os.listdir(curr_dir + "FriendImgs")
    x,y = 0,0
    for avatar in avatars:
        try:
            img = Image.open(curr_dir + "FriendImgs/" + avatar)
        except IOError:
            continue
        else:
            img = img.resize((50,50),Image.ANTIALIAS)
            image.paste(img, (x*50, y*50))
            x += 1
            if x==13:
                x = 0
                y += 1

    img = image.save(curr_dir + "WeChat_Friends.jpg")
