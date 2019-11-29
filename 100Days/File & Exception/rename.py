# -*- coding: UTF-8 -*-
import os

dir_name = 'export/'
figure_names = os.listdir(os.path.join(dir_name))

for name in figure_names:
    new_name = name[length:]    # 对原始文件名进行批量更改
    print(new_name)
    os.rename(dir_name + name,dir_name + new_name)
