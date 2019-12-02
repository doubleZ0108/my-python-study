'''
@program: server.py

@description: Server

@author: doubleZ

@create: 2019/12/02 
'''

import eel

@eel.expose
def my_python_func(data):       # 使用json传递数据
    print('my python function...')
    print(data)
    username, password = data['username'], data['password']
    print(username, password)


if __name__ == '__main__':
    eel.init('../web/')
    eel.start('index.html')
