from Piece import *

def test_different_pieces():
    first = Piece("black", (1, 2))
    second = Piece("black", (1, 3))
    assert first != second
    
