import time
import tkinter
import tkinter.messagebox

'''
这种情况下, 点击"下载"按钮后整个程序的其他部分都被阻塞, 用户此时啥也动不了
'''
def download():
    # 模拟下载任务需要花费10秒钟时间
    time.sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成!')


def show_about():
    tkinter.messagebox.showinfo('关于', 'This is a text.')


def main():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


def Handeler():
    # 把耗费时间的下载放到单独的线程中执行
    class DownloadTaskHandeler(Thread):
        def run(self):
            # 模拟下载任务需要花费10秒钟时间
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            button1.config(state=tkinter.NORMAL)


    def download():
        button1.config(state=tkinter.DISABLED)
        DownloadTaskHandeler(daemon=True).start()



    def show_about():
        tkinter.messagebox.showinfo('关于', 'This is a text.')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()
    

if __name__ == '__main__':
    # main()
    Handeler()
