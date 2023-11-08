import Piece

class Board:
    def __init__(self, SIZE = 10):
        self.board = [[None for i in range(SIZE)] for j in range(SIZE)]
        for i in range(1, SIZE - 1):
            self.board[0][i] = Piece("black")
            self.board[SIZE-1][i] = Piece("black")
            self.board[i][0] = Piece("white")
            self.board[i][SIZE-1] = Piece("white")
    
    def getBoard(self):
        return self.board