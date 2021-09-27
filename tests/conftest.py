from main import *
import pytest


@pytest.fixture
def matrix():
    g = [['X', 'X', 'X'], ['O', 'O', '_'], ['_', 'O', '_']]
    return g


@pytest.fixture
def str_to_matrix():
    gstr = 'XXXOO__O_'
    return gstr


@pytest.fixture
def win_o():
    g = input_to_matrix('XOOOXOXXO')
    s = 'O'
    return g, s


@pytest.fixture
def win_x():
    g = input_to_matrix('XOXOXOXXO')
    s = 'X'
    return g, s


@pytest.fixture
def draw():
    g = input_to_matrix('XOXOOXXXO')
    return g


@pytest.fixture
def game_finished():
    g = input_to_matrix('XOXOXOXXO')
    return g


@pytest.fixture
def game_not_finished():
    g = input_to_matrix('XO_OOX_X_')
    return g


@pytest.fixture
def game_impossible1():
    g = input_to_matrix('_O_X__X_X')
    return g


@pytest.fixture
def game_impossible2():
    g = input_to_matrix('XO_XO_XOX')
    return g


@pytest.fixture
def game_impossible3():
    g = input_to_matrix('_O_X__X_X')
    return g


@pytest.fixture
def game_impossible4():
    g = input_to_matrix('_OOOO_X_X')
    return g


@pytest.fixture
def valid_coord():
    i = ["1", "3"]
    return i


@pytest.fixture
def outofbounds_coord():
    i = ["1", "4"]
    return i


@pytest.fixture
def invalid_format_coord1():
    i = ["AA"]
    return i


@pytest.fixture
def invalid_format_coord2():
    i = ["11"]
    return i


@pytest.fixture
def invalid_format_coord3():
    i = ["1", "1", "1"]
    return i

@pytest.fixture
def invalid_format_coord4():
    i = ["one"]
    return i

@pytest.fixture
def occupied_coord():
    i = ["1", "1"]
    return i