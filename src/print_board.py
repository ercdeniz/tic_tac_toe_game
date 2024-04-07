import utils as u
def print_board(flag=0):
    if flag == 1:
        print(f" {1} | {2} | {3} ")
        print("---+---+---")
        print(f" {4} | {5} | {6} ")
        print("---+---+---")
        print(f" {7} | {8} | {9} ")
    else:
        print(f" {u.board[0]} | {u.board[1]} | {u.board[2]} ")
        print("---+---+---")
        print(f" {u.board[3]} | {u.board[4]} | {u.board[5]} ")
        print("---+---+---")
        print(f" {u.board[6]} | {u.board[7]} | {u.board[8]} ")