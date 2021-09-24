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
# TODO Game state draw
# TODO Game state X Win
# TODO Game state O Win
# TODO Game state impossible


def input_to_matrix(g_str):
    return [[g_str[i*3 + c] for c in range(3)] for i, r in enumerate(range(3))]


if __name__ == '__main__':
    # grid = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']] matrix format
    grid = "XOXOOXXXO"
    # grid = input_to_list(input("Enter cells:"))
    grid = (input_to_matrix(grid))
    print_grid(grid)

