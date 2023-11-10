from Piece import *

class Board:
    def __init__(self, SIZE = 10):
        """initialize a board of SIZE for the game"""
        self.size = SIZE
        self.board = [[None for i in range(SIZE)] for j in range(SIZE)]
        for i in range(1, SIZE - 1):
            self.board[0][i] = Piece("black", (0, i))
            self.board[SIZE-1][i] = Piece("black", (SIZE-1, i))
            self.board[i][0] = Piece("white", (i, 0))
            self.board[i][SIZE-1] = Piece("white", (i, SIZE-1))
    
    def getBoard(self):
        return self.board
    
    def numRow(self, Piece):
        """returns the number of pieces in a row as an integer"""
        therow = Piece.location[1]
        counter = 0
        for i in range(0, self.size):
            if self.board[therow][i] != None:
                counter += 1
        return counter


