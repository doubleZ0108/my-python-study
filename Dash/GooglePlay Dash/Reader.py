import pandas as pd
import plotly.graph_objs as go
import csv

def read_file():
    file=csv.reader(open('dataset\google-play-store-apps\googleplaystore.csv',encoding='utf-8'))
    
    return file

def file_filter(file, catagory_name, price_choice):
    newfile = []
    for row in file:
        if row[1]==catagory_name:
            if price_choice=='All':
                newfile.append(row)
            elif price_choice=='Free' and row[7]=='0':
                newfile.append(row)
            elif price_choice=='Paid' and row[7]!='0':
                newfile.append(row)

    return newfile


def get_size(file):
    size_catagory = ['0~300K','300K~600K','600K~900K','900K~25M','25M~50M','50M~75M','75M~100M','Varies with device']
    size_list = [0]*len(size_catagory)
    variesNum = 0
    for row in file:
        if row[4][-1]=='M':
            num = float(row[4][0:-1])
            size_list[int(num//25) + 3] += 1
        elif row[4][-1]=='k':
            num = float(row[4][0:-1])
            if num>900:
                size_list[3]+=1
            else:
                size_list[int(num//300)]+=1
        elif row[4]=='Varies with device':
            size_list[-1]+=1
        else:
            continue        # 去掉第一行的Size

    return [size_catagory, size_list]

def get_content_rating(file):
    content_rating_catagory = ['Everyone','Teen','Everyone 10+','Mature 17+','Adults only 18+','Unrated']
    content_rating_list = [0]*len(content_rating_catagory)

    for row in file:
        if row[8]!='Content Rating':
            content_rating_list[content_rating_catagory.index(row[8])]+=1

    return [content_rating_catagory, content_rating_list]

if __name__=='__main__':
    file = read_file()
    newfile = file
    newfile = file_filter(newfile,'ART_AND_DESIGN','Free')
    [size_catagory, size_list] = get_content_rating(newfile)
    for i in range(len(size_catagory)):
        print('{} {}'.format(size_catagory[i],size_list[i]))
