'''
回溯法

骑士巡逻:
    将一个马放在棋盘上，有什么路径能使它走遍棋盘上每一格呢？

分析:
    从起点开始, 按照马的规则移动到下一步, 再下一步,..., 如果能走遍则输出
    如果下一步的8个点都曾经走过了, 则退回到上一步往下个方向进入
'''

SIZE = 5
total = 0

def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4),end='')    # str对象才有center方法
        print()

def patroal(board, row, col,step=1):
    # 如果在棋盘上, 并且这步没走过 -> 走一下
    if row>=0 and col>=0 and row<SIZE and col<SIZE and board[row][col]==0:
        board[row][col] = step

        # 走遍棋盘了
        if step==SIZE**2:
            global total
            total += 1
            print(f'第{total}种走法: ')
            print_board(board)

        patroal(board,row-1,col+2,step+1)
        patroal(board,row-1,col-2,step+1)
        patroal(board,row-2,col-1,step+1)
        patroal(board,row-2,col+1,step+1)
        patroal(board,row+1,col-2,step+1)
        patroal(board,row+1,col+2,step+1)
        patroal(board,row+2,col-1,step+1)
        patroal(board,row+2,col+1,step+1)
        board[row][col] = 0     # 运行到这里说明8个方向都没最终走遍棋盘(如果走遍了,就会一直递归下去, 直到递归终止条件退出)

def main():
    board = [[0]*SIZE for _ in range(SIZE)]
    patroal(board,SIZE-1,SIZE-1)

if __name__ == "__main__":
    main()
