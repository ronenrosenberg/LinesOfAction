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
    
    def numRow(self, piece):
        """returns the number of pieces in a row as an integer"""
        theRow = piece.location[0]
        counter = 0
        for i in range(0, self.size):
            if self.board[theRow][i] != None:
                counter += 1
        return counter

    def numCol(self, piece):
        theCol = piece.location[1]
        counter = 0
        for i in range(0, self.size):
            if self.board[i][theCol] != None:
                counter += 1
        return counter
    
    def NumPosDiagonal(self, piece):
        (x, y) = Piece.location
        x -= 1; y -= 1
        counter = 0
        while x != 0 and y != 0:
            if self.board[x][y] != None:
                counter += 1
            x -= 1; y -=1

        (x, y) = Piece.location
        x += 1; y += 1
        while x != self.size-1 and y != self.size-1:
            if self.board[x][y] != None:
                counter += 1
            x += 1; y +=1

    def NumNegDiagonal(self, piece):
        (x, y) = Piece.location
        x -= 1; y += 1
        counter = 0
        while x != 0 and y != 0:
            if self.board[x][y] != None:
                counter += 1
            x -= 1; y +=1

        (x, y) = Piece.location
        x += 1; y -= 1
        while x != self.size-1 and y != self.size-1:
            if self.board[x][y] != None:
                counter += 1
            x += 1; y -=1

