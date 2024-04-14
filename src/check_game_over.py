import utils as u

def check_game_over():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows index
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns index
        [0, 4, 8], [2, 4, 6]  # Diagonals index
    ]
    if u.game_status == 'S':
        for condition in win_conditions:
            if u.board[condition[0]] == u.board[condition[1]] == u.board[condition[2]] != ' ':
                return True, 'You win!' if u.board[condition[0]] == u.player else 'Computer wins!'
        if ' ' not in u.board:
            return True, 'The game is a draw! Want a rematch?'
        return False, ''
    else:
        for condition in win_conditions:
            if u.board[condition[0]] == u.board[condition[1]] == u.board[condition[2]] != ' ':
                return True, 'Player 1 wins!' if u.board[condition[0]] == u.player else 'Player 2 wins!'
        if ' ' not in u.board:
            return True, 'The game is a draw! Want a rematch?'
        return False, ''