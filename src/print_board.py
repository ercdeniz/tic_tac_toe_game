import utils as u
def print_board(flag=0):
    board = u.board.copy()
    if flag == 1:
        print(f" {1} | {2} | {3} ")
        print("---+---+---")
        print(f" {4} | {5} | {6} ")
        print("---+---+---")
        print(f" {7} | {8} | {9} ")
    else:
        for i in range(9):
            if u.board[i] != ' ':
                if u.board[i] == 'X':
                    board[i] = u.RED + board[i] + u.RES
                else:
                    board[i] = u.BLUE + board[i] + u.RES
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")