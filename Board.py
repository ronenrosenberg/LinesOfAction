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
        
        #variables for recursivePieceSearch()
        self.blacklist = []
        self.totalConnectedPieces = 0
    
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
        theRow = piece.getLocation()[0]
        counter = 0
        for i in range(0, self.size):
            if self.board[theRow][i] != None:
                counter += 1
        return counter

    def numCol(self, piece):
        """returns the number of pieces in a column as an integer"""
        theCol = piece.getLocation()[1]
        counter = 0
        for i in range(0, self.size):
            if self.board[i][theCol] != None:
                counter += 1
        return counter
    
    def numPosDiagonal(self, piece):
        """returns the number of pieces in a positive diagonal as an integer"""
        
        # iterating from before <x,y> to bottom
        (x, y) = piece.getLocation()
        x -= 1; y -= 1
        counter = 0
        while x >= 0 and y >= 0:
            if self.board[x][y] != None:
                counter += 1
            x -= 1; y -=1

        # iterating from top to <x,y>
        (x, y) = piece.getLocation()
        while x <= self.size-1 and y <= self.size-1:
            if self.board[x][y] != None:
                counter += 1
            x += 1; y +=1
        
        return counter

    def numNegDiagonal(self, piece):
        """returns the number of pieces in a negative diagonal as an integer"""
        
        # iterating from before <x,y> to bottom
        (x, y) = piece.getLocation()
        x -= 1; y += 1
        counter = 0
        while x >= 0 and y <= self.size-1:
            if self.board[x][y] != None:
                counter += 1
            x -= 1; y +=1

        # iterating from top to <x,y>
        (x, y) = piece.getLocation()
        while x <= self.size-1 and y >= 0:
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
    
    #finds number of contiguous pieces
    def recursivePieceSearch(self, piece):
        "alters the value of total, counting the sum of a group of connected pieces"
        #current piece's (x, y)
        (currentPieceX, currentPieceY) = piece.getLocation()
        
        #creates list of all new pieces in 3*3 surrounding 
        newPieces = []
        for x in range (currentPieceX - 1, currentPieceX + 2):
            for y in range (currentPieceY - 1, currentPieceY + 2):
                #make sure we're checking possible indices
                if (x >= 0 and x < self.size and y >= 0 and y < self.size):
                    #(if square has a piece in it) and (this piece hasn't already been counted) and (is of the same team as calling piece)
                    if (self.board[x][y] != None) and (self.board[x][y] not in self.blacklist) and (piece.isSameTeam(self.board[x][y])):
                        self.blacklist.append(self.board[x][y])
                        self.recursivePieceSearch(self.board[x][y])
                        self.totalConnectedPieces += 1

    def findConnectedPieceSize(self, team):
        "Controller method for recursivePieceSearch()"
        #gets a piece on the board of the specified team
        #what piece we start with isn't important, b/c all pieces have to be connected for win condition
        for x in self.board:
            for y in x:
                if y != None and y.getTeam() == team:
                    piece = y
        
        #recursivePieceSearch() finds the number of contiguous pieces of the given team and assigns it to self.totalConnectedPieces
        self.recursivePieceSearch(piece)

        total = self.totalConnectedPieces

        #resets totalConnectedPieces and blacklist
        self.totalConnectedPieces = 0
        self.blacklist = []

        return total
    
    def range(self, piece):
        """returns a list of ordered pairs, containing all the locations that a piece can move to"""
        available = self.rangerow(piece) + self.rangecol(piece) + self.rangeposd(piece) + self.rangenegd(piece)
        return available

    def rangerow(self, piece):
        (x, y) = piece.getLocation()
        avrow = []
        #iterating through number in row
        row = self.numRow(piece)
        
        if y+row <= self.size-1:
            if self.board[x][y+row] == None:
                avrow.append((x,y+row))
                print ("<"+ str(x) + ", " + str(y+row) + ">")
            elif self.board[x][y+row].getTeam() != piece.getTeam():
                avrow.append((x,y+row))
                print ("<"+ str(x) + ", " + str(y+row) + ">")

            i=row-1
            while i>0:
                if self.board[x][y+i] != None:
                    if self.board[x][y+i].getTeam() != piece.getTeam():
                        while len(avrow) > 0:
                            avrow.pop(0)
                i-=1

        if y-row >= 0:
            if self.board[x][y-row] == None:
                avrow.append((x,y-row))
            elif self.board[x][y-row].getTeam() != piece.getTeam():
                avrow.append((x,y-row))
            i=row-1
            while i>0:
                if self.board[x][y-i] != None:
                    if self.board[x][y-i].getTeam() != piece.getTeam():
                        while len(avrow) > 0:
                            avrow.pop(0)
                i-=1

        return avrow

    def rangecol(self, piece):
        (x, y) = piece.getLocation()
        avcol = []
        #iterating through number in row
        col = self.numCol(piece)
        
        if x+col <= self.size-1:
            if self.board[x+col][y] == None:
                avcol.append((x+col,y))
            elif self.board[x+col][y].getTeam() != piece.getTeam():
                avcol.append((x+col,y))
            i=col-1
            while i>0:
                if self.board[x+i][y] != None:
                    if self.board[x+i][y].getTeam() != piece.getTeam():
                        while len(avcol) > 0:
                            avcol.pop(len(avcol)-1)
                i-=1

        if x-col >= 0:
            if self.board[x-col][y] == None:
                avcol.append((x-col,y))
            elif self.board[x-col][y].getTeam() != piece.getTeam():
                avcol.append((x-col,y))
            i=col-1
            while i>0:
                if self.board[x-i][y] != None:
                    if self.board[x-i][y].getTeam() != piece.getTeam():
                        while len(avcol) > 0:
                            avcol.pop(len(avcol)-1)
                i-=1

        return avcol

    def rangeposd(self, piece):
        (x, y) = piece.getLocation()
        avposd = []
        #iterating through number in row
        ack = self.numPosDiagonal(piece)
        
        if (x+ack <= self.size-1) and (y+ack <= self.size-1):
            if self.board[x+ack][y+ack] == None:
                avposd.append((x+ack,y+ack))
            elif self.board[x+ack][y+ack].getTeam() != piece.getTeam():
                avposd.append((x+ack,y+ack))
            i=ack-1
            while i>0:
                if self.board[x+i][y+i] != None:
                    if self.board[x+i][y+i].getTeam() != piece.getTeam():
                        while len(avposd) > 0:
                            avposd.pop(len(avposd)-1)
                i-=1

        if (x-ack >= 0) and (y-ack >= 0):
            if self.board[x-ack][y-ack] == None:
                avposd.append((x-ack,y-ack))
            elif self.board[x-ack][y-ack].getTeam() != piece.getTeam():
                avposd.append((x-ack,y-ack))
            i=ack-1
            while i>0:
                if self.board[x-i][y-i] != None:
                    if self.board[x-i][y-i].getTeam() != piece.getTeam():
                        while len(avposd) > 0:
                            avposd.pop(len(avposd)-1)
                i-=1

        return avposd

    def rangenegd(self, piece):
        (x, y) = piece.getLocation()
        avnegd = []
        #iterating through number in row
        ick = self.numNegDiagonal(piece)
        
        if (x+ick <= self.size-1) and (y-ick >= 0):
            if self.board[x+ick][y-ick] == None:
                avnegd.append((x+ick,y-ick))
            elif self.board[x+ick][y-ick].getTeam() != piece.getTeam():
                avnegd.append((x+ick,y+ick))
            i=ick-1
            while i>0:
                if self.board[x+i][y-i] != None:
                    if self.board[x+i][y-i].getTeam() != piece.getTeam():
                        while len(avnegd) > 0:
                            avnegd.pop(len(avnegd)-1)
                i-=1

        if (x-ick >= 0) and (y+ick <= self.size-1):
            if self.board[x-ick][y+ick] == None:
                avnegd.append((x-ick,y+ick))
            elif self.board[x-ick][y+ick].getTeam() != piece.getTeam():
                avnegd.append((x-ick,y+ick))
            i=ick-1
            while i>0:
                if self.board[x-i][y-i] != None:
                    if self.board[x-i][y-i].getTeam() != piece.getTeam():
                        while len(avnegd) > 0:
                            avnegd.pop(len(avnegd)-1)
                i-=1

        return avnegd 
    