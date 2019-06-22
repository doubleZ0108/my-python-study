from xpinyin import Pinyin
import faker

def Sort4Chinese(lis):  # 输入一个名字的列表
    pin = Pinyin()
    result = []
    for item in lis:
        result.append((pin.get_pinyin(item), item))
    result.sort()

    for i in range(len(result)):
        result[i] = result[i][1]

    return result

init = faker.Faker(locale='zh-cn')
pinyin = Pinyin()

if __name__=='__main__':
    words = [
"正风肃纪	264",
"作风建设	264",
"政治纪律	265",
"破窗效应	265",
"制度建设	265",
"标本兼治	265",
"廉政建设	265",
"腐败	265"]
    words = Sort4Chinese(words)

    print(words)



