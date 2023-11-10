from Board import *
from Piece import *

def test_different_boards():
    first = Board(10)
    second = Board(10)
    assert first != second

def test_num_row():
    first = Board(10)
    answer = Board.numRow(first.board[0][2])
    assert answer == 2