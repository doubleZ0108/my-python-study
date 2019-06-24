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

    # 读取原文件
    infile = open('nonSortFile.txt','r')
    words = []
    try: 
        for line in infile:
            words.append(line)
    finally:
        infile.close()

    # 去除原文件的空行
    new_words = filter(lambda str: str!='\n', words)

    # 按中文首字母排序
    new_words = Sort4Chinese(words)

    # 写入目标文件
    outfile = open('Sorted.txt','w')
    try:
        for line in new_words:
            outfile.write(line)
    finally:
        outfile.close()
