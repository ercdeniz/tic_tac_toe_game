import vars_and_board as vb

def check_game_over():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows index
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns index
        [0, 4, 8], [2, 4, 6]  # Diagonals index
    ]
    for condition in win_conditions:
        if vb.board[condition[0]] == vb.board[condition[1]] == vb.board[condition[2]] != ' ':
            return True, 'You win!' if vb.board[condition[0]] == vb.player else 'Computer wins!'
    if ' ' not in vb.board:
        return True, 'The game is a draw! Want a rematch?'
    return False, ''
