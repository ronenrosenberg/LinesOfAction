from Piece import *

class Board:
    def __init__(self, SIZE = 10):
        """initialize a board of SIZE for the game"""
        self.size = SIZE
        #create board
        self.board = [[None for i in range(SIZE)] for j in range(SIZE)]
        #place pieces on board
        for i in range(1, SIZE - 1):
            self.board[0][i] = Piece("black", (0, i))
            self.board[SIZE-1][i] = Piece("black", (SIZE-1, i))
            self.board[i][0] = Piece("white", (i, 0))
            self.board[i][SIZE-1] = Piece("white", (i, SIZE-1))
    
    def getBoard(self):
        "returns board as a 2D array"
        return self.board
    
    def move(self, piece, newLocationTuple):
        "moves a piece from one location to another"
        #old and new locations
        (oldX, oldY) = piece.getLocation()
        (x, y) = newLocationTuple

        #moves piece
        self.board[oldX][oldY] = None
        self.board[x][y] = piece

        #correct's piece's location attribute
        piece.setLocation(newLocationTuple)

    def numRow(self, piece):
        """returns the number of pieces in a row as an integer"""
        theRow = piece.getLocation()[1]
        counter = 0
        for i in range(0, self.size):
            if self.board[theRow][i] != None:
                counter += 1
        return counter

    def numCol(self, piece):
        """returns the number of pieces in a column as an integer"""
        theCol = piece.getLocation()[0]
        counter = 0
        for i in range(0, self.size):
            if self.board[i][theCol] != None:
                counter += 1
        return counter
    
    def numPosDiagonal(self, piece):
        """returns the number of pieces in a positive diagonal as an integer"""
        (x, y) = piece.getLocation()
        x -= 1; y -= 1
        counter = 0
        while x != 0 and y != 0:
            if self.board[x][y] != None:
                counter += 1
            x -= 1; y -=1

        (x, y) = piece.getLocation()
        while x != self.size-1 and y != self.size-1:
            if self.board[x][y] != None:
                counter += 1
            x += 1; y +=1
        
        return counter

    def numNegDiagonal(self, piece):
        """returns the number of pieces in a negative diagonal as an integer"""
        (x, y) = piece.getLocation()
        x -= 1; y += 1
        counter = 0
        while x != 0 and y != 0:
            if self.board[x][y] != None:
                counter += 1
            x -= 1; y +=1

        (x, y) = piece.getLocation()
        while x != self.size-1 and y != self.size-1:
            if self.board[x][y] != None:
                counter += 1
            x += 1; y -=1

        return counter
    
    def teamTotalPieces(self):
        """returns an ordered pair of white, and then black's, total pieces"""
        numWhite, numBlack = 0, 0
        for x in range(self.size):
            for y in range(self.size):
                #get a specific square of the board
                square = self.board[x][y]
                if square != None:
                    if square.getTeam() == "white":
                        numWhite += 1
                    else:
                        numBlack += 1
        return (numWhite, numBlack)
    
    def range(self, piece):
        """returns a list of ordered pairs, containing all the locations that a piece can move to."""
        availables = []
        (x, y) = piece.getLocation

        #iterating through number in row
        nah = self.numRow(piece)
        row = 0-nah #from negative to positive
        while row <= nah:
            if row != 0:
                if self.board[x][y+row] == None:
                    #if tile is empty, you can go!
                    availables.append((x, y+row))
                elif self.board[x][y+row].getTeam != piece.getTeam:
                    availables.append((x, y+row))
                    if row > 0:
                        # if u run into enemy on ur way away, u can't jump
                        row = nah
                    if row < 0:
                        # if u run into an enemy on ur way to, delete prev spaces
                        for i in range(nah+col):
                            availables.pop(len(availables)-1)
            row += 1

        nah = self.numCol(piece)
        col = 0-nah
        while col <= nah:
            if col != 0:
                if self.board[x+col][y] == None:
                    availables.append((x+col, y))
                elif self.board[x+col][y].getTeam != piece.getTeam:
                    availables.append((x+col, y))
                    if col > 0:
                        col = nah
                    if col < 0:
                        for i in range(nah+col):
                            availables.pop(len(availables)-1)
            col += 1

        nah = self.numPosDiagonal(piece)
        ack = 0-nah
        while ack <= nah:
            if ack != 0:
                if self.board[x+ack][y+ack] == None:
                    availables.append((x+ack, y+ack))
                elif self.board[x+ack][y+ack].getTeam != piece.getTeam:
                    availables.append((x+ack, y+ack))
                    if ack > 0:
                        ack = nah
                    if ack < 0:
                        for i in range(nah+ack):
                            availables.pop(len(availables)-1)
            ack += 1

        nah = self.numNegDiagonal(piece)
        ick = 0-nah
        while ick <= nah:
            if ick != 0:
                if self.board[x+ick][y-ick] == None:
                    availables.append((x+ick, y-ick))
                elif self.board[x+ick][y-ick].getTeam != piece.getTeam:
                    availables.append((x+ick, y-ick))
                    if ick > 0:
                        ick = nah
                    if ick < 0:
                        for i in range(nah+ick):
                            availables.pop(len(availables)-1)
            ick += 1

        return availables
    