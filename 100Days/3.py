
# 井字棋游戏
def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def Tic_Tac_Toe():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' ',
    }
    while True:
        curr_board = init_board.copy()
        turn = 'x'
        cnt = 0
        os.system('cls')
        print_board(curr_board)
        while cnt < 9:
            move = input('轮到%s走棋, 请输入位置' % turn)
            if(curr_board[move]==' '):
                curr_board[move] = turn
                cnt += 1
                turn = 'o' if turn=='x' else 'x'
            os.system('cls')
            print_board(curr_board)
        choice = input('再玩一局?(y|n)')
        if choice=='n': break

if __name__=="__main__":
    Tic_Tac_Toe()
