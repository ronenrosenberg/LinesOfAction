from Piece import *

def test_different_pieces():
    first = Piece("black", (1, 2))
    second = Piece("black", (1, 2))
    assert first != second
    
def test_pieces_team():
    thing = Piece("black", (1, 2))
    team = thing.getTeam()
    assert team == "black"

def test_location_pieces():
    first = Piece("black", (1, 2))
    location = first.getLocation()
    assert location == (1,2)
