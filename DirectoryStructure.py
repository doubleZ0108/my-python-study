def ReadFile(filename):
    # 读取原文件
    infile = open(filename)
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


if __name__=="__main__":
    file = ReadFile('origin.txt');
    for i in range(len(file)):
        file[i] = file[i].strip('\n');
        file[i] = file[i]+"    \n";
    
    WriteFile("target.txt",file);
