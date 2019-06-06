import pandas as pd
import plotly.graph_objs as go
import csv


def read_file():
    file = csv.reader(
        open('dataset\google-play-store-apps\googleplaystore.csv',
             encoding='utf-8'))

    return file


def file_filter(file, catagory_name, price_choice):
    newfile = []
    for row in file:
        if row[1] == catagory_name:
            if price_choice == 'All':
                newfile.append(row)
            elif price_choice == 'Free' and row[7] == '0':
                newfile.append(row)
            elif price_choice == 'Paid' and row[7] != '0':
                newfile.append(row)

    return newfile

def rating_filter(file, rating_value):
    newfile = []
    for row in file:
        if row[2]=='Rating':
            continue
        elif row[2]=='NaN':
            newfile.append(row)
        else:
            value = float(row[2])
            if value < rating_value:
                newfile.append(row)

    return newfile


def get_main(file):
    Reviews = []
    Installs = []
    App = []
    
    for row in file:
        if row[0]!='App':
            App.append(row[0])
        
        if row[3]!='Reviews':
            Reviews.append(row[3])
        
        if row[5]!='Installs':
            Installs.append(row[5])
    
    return[Reviews, Installs, App]

def get_size(file):
    size_catagory = [
        '0~300K', '300K~600K', '600K~900K', '900K~25M', '25M~50M', '50M~75M',
        '75M~100M', 'Varies with device'
    ]
    size_list = [0] * len(size_catagory)
    variesNum = 0
    for row in file:
        if row[4][-1] == 'M':
            num = float(row[4][0:-1])
            size_list[int(num // 25) + 3] += 1
        elif row[4][-1] == 'k':
            num = float(row[4][0:-1])
            if num > 900:
                size_list[3] += 1
            else:
                size_list[int(num // 300)] += 1
        elif row[4] == 'Varies with device':
            size_list[-1] += 1
        else:
            continue  # 去掉第一行的Size

    return [size_catagory, size_list]


def get_content_rating(file):
    content_rating_catagory = [
        'Everyone', 'Teen', 'Everyone 10+', 'Mature 17+', 'Adults only 18+',
        'Unrated'
    ]
    content_rating_list = [0] * len(content_rating_catagory)

    _content_rating_catagory = []
    _content_rating_list = []

    for row in file:
        content_rating_list[content_rating_catagory.index(row[8])] += 1

    # for i in range(len(content_rating_catagory)):
    #     if content_rating_list[i] > 0:
    #         _content_rating_catagory.append(content_rating_catagory[i])
    #         _content_rating_list.append(content_rating_list[i])

    # return [_content_rating_catagory, _content_rating_list]
    return [content_rating_catagory, content_rating_list]


def get_price(file):
    price_catagory = ['0','$1~$50','$50~$100','$100~$150','$150~$200',
    '$200~$250','$250~$300','$300~$350','$350~$400']
    price_list = [0] * (len(price_catagory))

    for row in file:
        if row[7] == 'Price':
            continue
        elif row[7] == '0':
            price_list[0] += 1
        else:
            price = int(float(row[7][1:])/50)
            price_list[price] += 1
    
    return [price_catagory,price_list]


if __name__ == '__main__':
    file = read_file()
    # [price_catagory, price_list] = get_price(file)
    # for i in range(len(price_catagory)):
    #     print('{} {}'.format(price_catagory[i], price_list[i]))
    
