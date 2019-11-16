# -*- coding: UTF-8 -*-
'''
原始图片名:
图 xxx.png
表 yyy.png
'''

import os

dir_name = 'figure/'
table_name = "表"
map_name = "图"
figure_names = os.listdir(os.path.join(dir_name))
for name in figure_names:
    if name[0:3]==table_name:
        new_name = 'table_'+name[4:]
    elif name[0:3]==map_name:
        new_name = 'figure_'+name[4:]
    print(new_name)
    os.rename(dir_name + name,dir_name + new_name)
