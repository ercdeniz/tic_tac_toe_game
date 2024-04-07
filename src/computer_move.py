import random
import utils as u

def computer_move():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows index
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns index
        [0, 4, 8], [2, 4, 6]  # Diagonals index
    ]
    for condition in win_conditions:
        if u.board[condition[2]] == " " and (u.board[condition[0]] == u.board[condition[1]] == u.computer):
            return condition[2]
        if u.board[condition[1]] == " " and (u.board[condition[0]] == u.board[condition[2]] == u.computer):
            return condition[1]
        if u.board[condition[0]] == " " and (u.board[condition[1]] == u.board[condition[2]] == u.computer):
            return condition[0]
        if u.board[condition[2]] == " " and (u.board[condition[0]] == u.board[condition[1]] == u.player):
            return condition[2]
        if u.board[condition[1]] == " " and (u.board[condition[0]] == u.board[condition[2]] == u.player):
            return condition[1]
        if u.board[condition[0]] == " " and (u.board[condition[1]] == u.board[condition[2]] == u.player):
            return condition[0]
    return random.randint(0, 8)
