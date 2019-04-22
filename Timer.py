import threading
import time

def fun_timer():
    print('Hello Timer!')
    global timer

    # 必须在定时器执行函数内部重复构造定时器
    timer = threading.Timer(2.0, fun_timer)  # 之后是2s执行一次
    timer.start()


if __name__ == "__main__":
    timer = threading.Timer(1, fun_timer)  # 第一次执行是1s之后
    timer.start()

    time.sleep(15)     # 15s之后停止定时器
    print("Timer is end...")
    timer.cancel()
