from main import *


def test_print_grid(matrix):
    game = Game('X')
    game.m = matrix
    assert game.print_grid() == """---------
| X X X |
| O O _ |
| _ O _ |
---------"""


# when the grid has three O’s in a row grid, player
def test_is_win_o(win_o):
    game = Game('X')
    game.m = win_o[0]
    assert game.is_win(win_o[1]) is True


# when the grid has three X’s in a row grid, player
def test_is_win_x(win_x):
    game = Game('X')
    game.m = win_x[0]
    assert game.is_win(win_x[1]) is True


# when no side has a three in a row and the grid has no empty cells.
def test_is_draw(draw):
    game = Game('X')
    game.m = draw
    assert game.is_draw() is True


def test_is_impossible1(game_impossible1):
    game = Game('X')
    game.m = game_impossible1
    assert game.is_impossible() is True


def test_is_impossible2(game_impossible2):
    game = Game('X')
    game.m = game_impossible2
    assert game.is_impossible() is True


def test_is_impossible3(game_impossible3):
    game = Game('X')
    game.m = game_impossible3
    assert game.is_impossible() is True


def test_is_impossible4(game_impossible4):
    game = Game('X')
    game.m = game_impossible4
    assert game.is_impossible() is True


def test_input_to_matrix(str_to_matrix):
    assert input_to_matrix(str_to_matrix) == [['X', 'X', 'X'], ['O', 'O', '_'], ['_', 'O', '_']]


def test_is_finished(game_finished, game_not_finished):
    game = Game('X')
    game.m = game_finished
    assert game.is_finished() is True
    game.m = game_not_finished
    assert game.is_finished() is False


def test_no_s(matrix):
    game = Game('X')
    game.m = matrix
    assert game.no_s('X') == 3


def test_game_result_x_win(win_x):
    game = Game('X')
    game.m = win_x[0]
    assert game.game_result() == "X wins"


def test_game_result_o_win(win_o):
    game = Game('X')
    game.m = win_o[0]
    assert game.game_result() == "O wins"


def test_game_result_draw(draw):
    game = Game('X')
    game.m = draw
    assert game.game_result() == "Draw"


def test_game_result_impossible(game_impossible1):
    game = Game('X')
    game.m = game_impossible1
    assert game.game_result() == "Impossible"


def test_game_result_not_finished(game_not_finished):
    game = Game('X')
    game.m = game_not_finished
    assert game.game_result() == "Game not finished"


def test_validate_input(valid_coord):
    game = Game('X')
    game.coords = valid_coord
    assert game.validate_coords() is True


def test_validate_input_outofbounds(outofbounds_coord):
    game = Game('X')
    game.coords = outofbounds_coord
    assert game.validate_coords() is False


# "AA"
def test_validate_input_wrongformat1(invalid_format_coord1):
    game = Game('X')
    game.coords = invalid_format_coord1
    assert game.validate_coords() is False


# "11" no space
def test_validate_input_wrongformat2(invalid_format_coord2):
    game = Game('X')
    game.coords = invalid_format_coord2
    assert game.validate_coords() is False


# "1 1 1" three numbers
def test_validate_input_wrongformat3(invalid_format_coord3):
    game = Game('X')
    game.coords = invalid_format_coord3
    assert game.validate_coords() is False


def test_analyse_move_occupied(occupied_coord, game_not_finished):
    game = Game('X')
    game.coords = occupied_coord
    game.m = game_not_finished
    game.update_index()
    assert game.is_empty() is False


def test_analyse_move_empty(valid_coord, game_not_finished):
    game = Game('X')
    game.coords = valid_coord
    game.m = game_not_finished
    game.update_index()
    assert game.is_empty() is True


def test_update_grid(game_not_finished, valid_coord):
    game = Game('X')
    game.m = game_not_finished
    game.coords = valid_coord
    game.update_index()
    game.update_grid()
    assert game.m == [['X', 'O', 'X'], ['O', 'O', 'X'], ['_', 'X', '_']]


def test_update_coods(valid_coord):
    game = Game('X')
    game.coords = valid_coord
    game.update_index()
    assert game.idx == [0, 2]


# "AA"
def test_output_error1(invalid_format_coord1):
    game = Game('X')
    game.coords = invalid_format_coord1
    game.validate_coords()
    assert game.output_error() == 'You should enter numbers!'


# "14" - this could be improved two values
def test_output_error2(outofbounds_coord):
    game = Game('X')
    game.coords = outofbounds_coord
    game.validate_coords()
    assert game.output_error() == 'Coordinates should be from 1 to 3!'

# "one" - this could be improved two values
def test_output_error3(invalid_format_coord4):
    game = Game('X')
    game.coords = invalid_format_coord4
    game.validate_coords()
    assert game.output_error() == 'You should enter numbers!'
