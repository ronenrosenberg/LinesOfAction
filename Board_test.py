from Board import *
from Piece import *

def test_different_boards():
    first = Board(10)
    second = Board(10)
    assert first != second

def test_num_row():
    board = Board(10)
    piece = board.getBoard()[0][2]
    answer = board.numRow(piece)
    assert answer == 8

def test_num_col():
    board = Board(10)
    piece = board.getBoard()[2][0]
    answer = board.numCol(piece)
    assert answer == 8

def test_num_pos_diagonal():
    board = Board(10)
    piece = board.getBoard()[2][0]
    answer = board.numPosDiagonal(piece)
    assert answer == 2

def test_num_neg_diagonal():
    board = Board(10)
    piece = board.getBoard()[2][0]
    answer = board.numNegDiagonal(piece)
    assert answer == 2