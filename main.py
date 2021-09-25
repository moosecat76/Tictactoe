# Tic Tac Toe

def print_grid(g):
    out = '---------\n'
    for row in range(3):
        out += '| '
        for col in range(3):
            out += f'{g[col][row]} '
        out += '|\n'
    out += '---------'
    print(out)


# TODO Game state not finished
# when neither side has three in a row but the grid still has empty cells.
def is_finshed():
    pass


# TODO Game state O Win
# when the grid has three O’s in a row.
def is_win_o():
    pass


# TODO Game state X Win
# when the grid has three X’s in a row.
def is_win_x():
    pass


# TODO Game state draw
# when no side has a three in a row and the grid has no empty cells.
def is_draw():
    pass


# when the grid has three X’s in a row as well
# as three O’s in a row, or there are a lot more
# X's than O's or vice versa (the difference
# should be 1 or 0; if the difference is 2 or
# more, then the game state is impossible).
def is_impossible():
    pass
# TODO Game state impossible


def input_to_matrix(g_str):
    return [[g_str[i*3 + c] for c in range(3)] for i, r in enumerate(range(3))]

# Apply rule logic
# Rules
# In this stage, we will assume that either X or O can start the game.
# You can choose whether to use a space or underscore _ to print empty cells.


if __name__ == '__main__':
    # grid = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']] matrix format
    grid = "XOXOOXXXO"
    # grid = input_to_list(input("Enter cells:"))
    grid = (input_to_matrix(grid))
    print_grid(grid)

