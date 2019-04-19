'''
“Make a script both importable and executable”

- 如果直接在这个脚本里运行, 则会输出 This is __main__, 也就是调用了main()函数
  - 或者在命令行直接 python this.py
- 如果是被import过来的, 则不会调用main(), 也就是不会进入 if __name__ == '__main__': 后面的语句
  因为此时该.py文件是__main__
  - 或命令行 python -> import myfirst -> xx.__name__ || __name__

用处:
  调试代码的时候，在”if __name__ == '__main__'“中加入一些我们的调试代码，
  让外部模块调用的时候不执行我们的调试代码
  但是如果我们想排查问题的时候，直接执行该模块文件，调试代码能够正常运行！
  
'''

def main():
    print('This is ', __name__)


if __name__ == '__main__':
    main()
