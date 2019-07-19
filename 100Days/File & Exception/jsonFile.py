import json

# JSON格式
'''
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
'''


'''
序列化: 将数据结构或对象状态转换为可以存储和传输的形式
        在需要的时候能够回复得到原来的状态
'''
def writeJSONFile():
    userInfo_dict = {
        "admin_id": "100003",
        "admin_avatar": "avatar_path",
        "admin_nickname": "\u6211\u53EB\u7528\u62374",
        "all_users": [{
            "user_id": "100000",
            "user_nickname": "\u6211\u53EB\u7528\u62371",
            "user_avatar": "avatar_path",
            "user_follow": 3,
            "user_fans": 3,
            "user_signature": "\u7528\u62371\u7684\u4E2A\u6027\u7B7E\u540D"
        }, {
            "user_id": "100001",
            "user_nickname": "\u6211\u53EB\u7528\u62372",
            "user_avatar": "avatar_path",
            "user_follow": 2,
            "user_fans": 2,
            "user_signature": "\u7528\u62372\u7684\u4E2A\u6027\u7B7E\u540D"
        }, {
            "user_id": "100002",
            "user_nickname": "\u6211\u53EB\u7528\u62373",
            "user_avatar": "avatar_path",
            "user_follow": 2,
            "user_fans": 2,
            "user_signature": "\u7528\u62373\u7684\u4E2A\u6027\u7B7E\u540D"
        }]
    }

    try:
        with open('userInfo.json', 'w', encoding='utf-8') as fs:
            json.dump(userInfo_dict, fs)
    except IOError as e:
        print(e)

    print('DONE!')

'''
反序列化
'''
def readJSONFile():
    with open('Resources/userInfo.json') as f:
        userInfo = json.load(f)
        print(userInfo['admin_id'])
        print(userInfo['admin_avatar'])
        print(userInfo['admin_nickname'])
        for user in userInfo['all_users']:
            print(user['user_id'])
            print(user['user_nickname'])
            print(user['user_avatar'])
            print(user['user_follow'])
            print(user['user_fans'])
            print(user['user_signature'])


if __name__ == "__main__":
    writeJSONFile()
    readJSONFile()
