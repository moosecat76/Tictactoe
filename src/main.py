# Tic Tac Toe

def print_grid(g):
    out = '---------\n'
    for row in range(3):
        out += '| '
        for col in range(3):
            out += f'{g[col][row]} '
        out += '|\n'
    out += '---------'
    return out


# when the grid has three O’s in a row.
def is_win(m, s):
    # test each row
    for row in range(3):
        r = is_row_win(m, row, s)
        if r is True:
            return r
    # test each col
    for col in range(3):
        r = is_col_win(m, col, s)
        if r is True:
            return r
    # test the two diagonals
    return is_diagonal_win(m, s)


# when no side has a three in a row and the grid has no empty cells.
def is_draw(m):
    if is_finished(m) is True:
        if is_win(m, 'O') is True:
            r = False
        elif is_win(m, 'X') is True:
            r = False
        else:
            r = True
    else:
        r = False
    return r


# when neither side has three in a row but the grid still has empty cells.
def is_finished(m):
    if not is_win(m, 'O') and not is_win(m, 'X') and (no_s(m, '_') > 0 or no_s(m, ' ')):
        return False
    return True


def no_s(m, s):
    r = len([symbol for row in m for symbol in row if symbol == s])
    return r


def is_impossible(m):
    #  Too many turns
    if abs(no_s(m, 'O') - no_s(m, 'X')) >= 2:
        return True
    # Both sides win
    if is_win(m, 'O') and is_win(m, 'X'):
        return True
    return False


def game_result(m):
    r = ''
    players = ['X', 'O']
    for player in players:
        if is_win(m, player):
            r = f'{player} wins'
    if is_draw(m):
        r = 'Draw'
    if not is_finished(m):
        r = 'Game not finished'
    if is_impossible(m):
        r = 'Impossible'
    return r


def input_to_matrix(g_str):
    return [[g_str[i*3 + c] for c in range(3)] for i, r in enumerate(range(3))]


# helpers
def is_row_win(m, row, s):
    if m[row][0] == s and m[row][1] == s and m[row][2] == s:
        return True
    else:
        return False


def is_col_win(m, col, s):
    if m[0][col] == s and m[1][col] == s and m[2][col] == s:
        return True
    else:
        return False


def is_diagonal_win_forward(m, s):
    if m[0][2] == s and m[1][1] == s and m[2][0] == s:
        return True
    else:
        return False


def is_diagonal_win_backward(m, s):
    if m[0][0] == s and m[1][1] == s and m[2][2] == s:
        return True
    else:
        return False


def is_diagonal_win(m, s):
    if is_diagonal_win_forward(m, s) or is_diagonal_win_backward(m, s):
        return True
    else:
        return False


# Apply rule logic
# Rules
# In this stage, we will assume that either X or O can start the game.
# You can choose whether to use a space or underscore _ to print empty cells.
if __name__ == '__main__':
    # grid = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']] matrix format
    grid = input("Enter cells:")
    grid = (input_to_matrix(grid))
    print(print_grid(grid))
    print(game_result(grid))
