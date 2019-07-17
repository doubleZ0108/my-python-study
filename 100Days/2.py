# 跑马灯
import os
import time

def marquee():
    content = "This is double Z!"
    while True:
        os.system('cls')
        print(content)

        time.sleep(0.2)
        content = content[1:] + content[0]

# 返回列表中最大和第二大的元素的值
def max2(li):
    m1,m2 = (li[0],li[1]) if li[0]>li[1] else (li[1],li[0])
    for index in range(2,len(li)):
        if li[index]>m1:
            m2 = m1
            m1 = li[index]
        elif li[index]>m2:
            m2 = li[index]

    return m1,m2


# 计算指定的年月日是一年的第几天
def is_leap_year(year):
    '''
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True, 平年返回False
    '''
    return (year%4==0 and year%100!=0) or year%400==0 

def which_day(year, month, date):
    '''
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    '''
    days_of_month = [           # days_of_month返回的是两个天数列表中的一个
        [31,28,31,30,31,30,31,31,30,31,30,31],
        [31,29,31,30,31,30,31,31,30,31,30,31]
    ][is_leap_year(year)]
    print(days_of_month)
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


# 打印杨辉三角形
def Pascal_Triangle(num):
    pt = [[]] * num
    for row in range(len(pt)):
        pt[row] = [None] * (row+1)
        for col in range(len(pt[row])):
            if col==0 or col==row:
                pt[row][col] = 1
            else:
                pt[row][col] = pt[row-1][col] + pt[row-1][col-1]
            print(pt[row][col],end=' ')
        print()

if __name__=="__main__":
    marquee()

    li = [2,6,1,7,123,765,23,0,-64,5]
    (m1,m2) = max2(li)
    print(m1,m2)

    print(which_day(2019,7,18))
    print(which_day(2000,1,8))

    Pascal_Triangle(8)
