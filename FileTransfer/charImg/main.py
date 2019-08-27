def handleFile():
    with open('that.txt', 'w', encoding='utf-8') as outf:
        with open('this.txt', mode='r') as inf:
            for line in inf:
                line = line.strip()
                newline = "printf(\"" + line + "\\n\");" + '\n'
                outf.write(newline)

if __name__ == "__main__":
    handleFile()
