'''
@program: server.py

@description: Server

@author: doubleZ

@create: 2019/12/02 
'''
import eel

'''处理js传来的数据'''
@eel.expose
def my_python_func_receive_data(data):       # 使用json传递数据
    print('my python function...')
    print(data)
    username, password = data['username'], data['password']
    print(username, password)


'''处理js传来的数据并返回'''
@eel.expose
def my_python_func_send_data(origin_data):
    print('从js中传入的原始数据' + origin_data)
    username, password = 'doubleZ', '77777'
    data = {
        'username': username,
        'password': password
    }
    return data


if __name__ == '__main__':
    eel.init('../web/')         # 存放静态网页的根目录
    eel.start('index.html')     # 启动server时的初始界面
