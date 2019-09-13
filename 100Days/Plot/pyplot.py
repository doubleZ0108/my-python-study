import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def func(x):
    return x**2


if __name__=='__main__':
    li_x = [i for i in range(10)]
    li_y = list(map(func, li_x))

    plt.figure()
    plt.plot(li_x, li_y)
    plt.xlabel('Waiting Position')      # 中文无法显示
    plt.ylabel('Waiting Time')
    plt.title('Function Name')
    plt.show()
