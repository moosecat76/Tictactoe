# Tic Tac Toe

class Game:
    m = []  # matix - game play state
    player = ''  # Player plays as X
    coords = []  # Entered coordinates
    idx = []  # index in matrix - ie. one less that coords
    valid_coords = False
    errors = []

    def __init__(self, player):
        self.m = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.player = 'X'

    def main(self):
        print(self.print_grid())
        self.take_turn()

    def take_turn(self):
        while not self.valid_coords:
            self.coords = str.split(input("Enter the coordinates: "), " ")
            if self.validate_coords():
                self.update_grid()
            if not self.valid_coords:
                self.output_error()
        print(self.print_grid())
        if self.is_finished():
            print(self.game_result())
        else:
            self.switch_player()
            self.take_turn()
        pass

    def switch_player(self):
        self.valid_coords = False
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def print_grid(self):
        out = '---------\n'
        for row in range(3):
            out += '| '
            for col in range(3):
                out += f'{self.m[row][col]} '
            out += '|\n'
        out += '---------'
        return out

    # when the grid has three O’s in a row.
    def is_win(self, s):
        # test each row
        for row in range(3):
            r = self.is_row_win(row, s)
            if r is True:
                return r
        # test each col
        for col in range(3):
            r = self.is_col_win(col, s)
            if r is True:
                return r
        # test the two diagonals
        return self.is_diagonal_win(s)

    # when no side has a three in a row and the grid has no empty cells.
    def is_draw(self):
        if not self.is_finished():
            return False

        if self.is_finished() is True:
            if self.is_win('O') is True:
                r = False
            elif self.is_win('X') is True:
                r = False
            else:
                r = True
        else:
            r = False
        return r

    # when neither side has three in a row but the grid still has empty cells.
    def is_finished(self):
        if not self.is_win('O') and not self.is_win('X') and (self.no_s('_') > 0 or self.no_s(' ')):
            return False
        return True

    def no_s(self, s):
        r = len([symbol for row in self.m for symbol in row if symbol == s])
        return r

    def is_impossible(self):
        #  Too many turns
        if abs(self.no_s('O') - self.no_s('X')) >= 2:
            return True
        # Both sides win
        if self.is_win('O') and self.is_win('X'):
            return True
        return False

    def game_result(self):
        r = ''
        players = ['X', 'O']
        for player in players:
            if self.is_win(player):
                r = f'{player} wins'
        if self.is_draw():
            r = 'Draw'
        if not self.is_finished():
            r = 'Game not finished'
        if self.is_impossible():
            r = 'Impossible'
        return r

    # test for out of bounds
    # test for co-ordinate
    def validate_coords(self):
        numeric = False
        inbounds = False
        valid = False
        if len(self.coords) == 2:
            if self.coords[0].isnumeric() and self.coords[1].isnumeric():
                numeric = True
                if 0 < int(self.coords[0]) <= 3 and 0 < int(self.coords[1]) <= 3:
                    inbounds = True
                else:
                    self.log_error('Coordinates should be from 1 to 3!')
            else:
                self.log_error('You should enter numbers!')
        else:
            self.log_error('You should enter numbers!')
        if numeric and inbounds:
            valid = True
            self.update_index()
        return valid

    def output_error(self):
        if len(self.errors) > 0:
            out = self.errors[-1]
            print(out)
            return out

    def log_error(self, message):
        self.errors.append(message)

    def update_index(self):
        self.idx = [int(self.coords[0]) - 1, int(self.coords[1]) - 1]

    # Check if position occupied
    def is_empty(self):
        result = False
        current_value = self.m[self.idx[0]][self.idx[1]]
        if (current_value == "_") or (current_value == " "):
            result = True
        return result

    def update_grid(self):
        if not self.is_empty():
            self.log_error('This cell is occupied! Choose another one!')
            return False
        self.m[self.idx[0]][self.idx[1]] = self.player
        self.valid_coords = True

    # helpers
    def is_row_win(self, row, s):
        return self.m[row][0] == s and self.m[row][1] == s and self.m[row][2] == s

    def is_col_win(self, col, s):
        if self.m[0][col] == s and self.m[1][col] == s and self.m[2][col] == s:
            return True
        else:
            return False

    def is_diagonal_win_forward(self, s):
        if self.m[0][2] == s and self.m[1][1] == s and self.m[2][0] == s:
            return True
        else:
            return False

    def is_diagonal_win_backward(self, s):
        if self.m[0][0] == s and self.m[1][1] == s and self.m[2][2] == s:
            return True
        else:
            return False

    def is_diagonal_win(self, s):
        if self.is_diagonal_win_forward(s) or self.is_diagonal_win_backward(s):
            return True
        else:
            return False


# static methods
def input_to_matrix(g_str):
    allowed = [" ", "_", "X", "O"]
    if(not len(g_str) == 9) or not [ele for ele in allowed if(ele in g_str)]:
        exit(0)
    return [[g_str[i * 3 + c] for c in range(3)] for i, r in enumerate(range(3))]


if __name__ == '__main__':
    # grid = [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']] matrix format

    ttt = Game('X')
    ttt.main()
