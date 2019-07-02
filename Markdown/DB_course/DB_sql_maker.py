def ReadFile(filename):
    # 读取原文件
    infile = open(filename,encoding='UTF-8')
    words = []
    try: 
        for line in infile:
            words.append(line)
    finally:
        infile.close()

    # 去除原文件的空行
    # new_words = filter(lambda str: str!='\n', words)
    return words

def WriteFile(filename, file):
    outfile = open(filename,'w')
    try:
        for line in file:
            outfile.write(line)
    finally:
        outfile.close()

def isChinese(ch):
    return '\u4e00' <= ch <= '\u9fff'

def Markdown_Maker(file, main_topic):
    new_file = []
    last_line = file[0]
    flag = True

    for line in file:
        line = line.strip('\n')     #先把所有行尾换行去掉
        if line=='':
            pass
        # 如果是注释
        elif line[0]=='-':
            line = line.strip('-')

            #如果是大块知识点
            if line[0]=='[':
                line = line.strip('[')
                line = line.strip(']')
                if line in main_topic:
                    line = '## '+line
                else:
                    line = '### '+line
            #如果是例子
            elif line[0].isdigit():
                line = '#### '+line
        #如果是sql语句
        elif flag and (line[0].isupper() or line=='(' or (line[0]=='(' and line[1].isupper())) :
            line = '```sql\n'+line
            flag = False
        elif (not flag) and line[-1]==';':
            line = line+'\n```'
            flag = True
        
        line = line+'\n'
        new_file.append(line)

    return new_file
            

if __name__=='__main__':
    main_topic = [
        '基础查询',
        'where子句谓词',
        '嵌套子查询',
        'from子句中的子查询',
        '删除',
        '插入',
        '更新',
        '视图 -> view',
        '函数'
    ]
    file = ReadFile('origin.txt')

    new_file = Markdown_Maker(file, main_topic)
    new_file.insert(0,'# 数据库SQL语句练习\n')
    new_file.insert(1,'[TOC]\n')

    WriteFile('DB.md',new_file)

    print("All done!")
