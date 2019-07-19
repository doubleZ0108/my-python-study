def writeFile():
    with open('this.txt', 'w', encoding='utf-8') as f:
        for i in range(10):
            f.write(str(i) + '\n')
            
if __name__ == "__main__":
    writeFile()
