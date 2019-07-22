import os
import sys
import requests

if __name__ == "__main__":
    # 网络图片的地址
    url = 'https://upload-images.jianshu.io/upload_images/12014150-8e8240e83f9ce72e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240'
    resp = requests.get(url)
    filename = 'figure1'

    
    # 获取当前路径
    curr_dir = os.getcwd()
    # 将图片保存到当前路径下的Figure文件夹中
    save_path = curr_dir + "\\Figure\\"

    # 在本地创建一个目录用于存储图像
    if not os.path.exists(save_path):    # 如果Figure目录不存在就创建一个
        os.mkdir(save_path)


    # 下载网络图片并存于本地
    with open(save_path + filename + '.png','wb') as f:
        f.write(resp.content)
