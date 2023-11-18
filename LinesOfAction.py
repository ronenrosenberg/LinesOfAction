from Board import *
from Piece import *
import stddraw

SIZE = 8

class LinesOfAction:
    def __init__(self, SIZE = 8):
        #the actual 2D array
        self.board = Board(SIZE)

        #useful for drawing
        self.SIZE = SIZE
        self.SIDE = 1.0/SIZE
        self.HALF = self.SIDE/2.0

        #logic variables
        self.state = "idle"
        self.selected = None
        self.currentTeam = "black"
        self.legalJumps = []

    def display(self):
        """draws a frame of the board in a given state"""
        stddraw.clear()

        #a few definitions
        size = self.SIZE
        side = self.SIDE
        half = self.HALF

        #blue background
        stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
        stddraw.filledSquare(0, 0, 1)
        #draw the board
        for x in range(size):
            for y in range(size):
                #get a specifc square of the board
                square = self.board.getBoard()[x][y]
                #if there's a piece on the square
                if (square != None):
                    #draw white piece
                    if square.getTeam() == "white":
                        stddraw.setPenColor(stddraw.WHITE)
                        stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                    else: #otherwise draw the black piece
                        stddraw.setPenColor(stddraw.BLACK)
                        stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                #draw black borders
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.square(x*side + half, y*side + half, half)
                
        #as long as state isn't idle, will grab click location
        if self.state != "idle":
            x = round((stddraw.mouseX() - half)/side)
            y = round((stddraw.mouseY() - half)/side)

        #state activated when there's been a click
        if self.state == "picking":
            atClickLocation = self.board.getBoard()[x][y]
            if  atClickLocation != None and atClickLocation.getTeam() == self.currentTeam: #makes sure that clicked square has a piece in it
                #highlights piece
                stddraw.setPenColor(stddraw.YELLOW)
                stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.5)
                #draw white piece
                if atClickLocation.getTeam() == "white":
                    stddraw.setPenColor(stddraw.WHITE)
                    stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                else: #otherwise draw the black piece
                    stddraw.setPenColor(stddraw.BLACK)
                    stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                
                self.legalJumps = self.board.range(atClickLocation)
                for coord in self.legalJumps:
                    (x, y) = coord
                    stddraw.setPenColor(stddraw.YELLOW)
                    stddraw.filledSquare(x*side + half, y*side + half, half * 0.93)
                    if self.board.getBoard()[x][y] != None:
                        if self.board.getBoard()[x][y].getTeam() == "white":
                            stddraw.setPenColor(stddraw.WHITE)
                            stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                        elif self.board.getBoard()[x][y].getTeam() == "black":
                            stddraw.setPenColor(stddraw.BLACK)
                            stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)

                #piece is "selected"
                self.selected = atClickLocation

            else: #if no piece has been selected, go back to idle
                self.state = "idle"
    
        #state activated on a second click, to move the piece to the second click
        if self.state == "moving":
            jumpLocation = self.board.getBoard()[x][y]
            #if just clicking to a different piece on the same team, reset to picking state with that piece
            if (jumpLocation != None) and (jumpLocation.isSameTeam(self.selected)):
                self.selected = self.board.getBoard()[x][y]
                self.state = "picking"
            #if clicking on non-valid location, resets back to idle
            elif (x, y) not in self.legalJumps:
                #resets logic variables, goes back to idle
                self.state = "idle"
                self.selected = None
                self.legalJumps = []
            #otherwise move the piece and reset to idle
            else:
                self.board.move(self.selected, (x, y))
                #resets logic variables
                self.state = "idle"
                self.selected = None
                self.legalJumps = []

                #flips to opposite team's turn
                if self.currentTeam == "black":
                    self.currentTeam = "white"
                else:
                    self.currentTeam = "black"
        
        #don't question this line, it just makes it work
        stddraw.show(0)
    
    #checks for win state
    def won(self):
        #gets total # of black and white pieces on board
        numWhite, numBlack = self.board.teamTotalPieces()
        #checks if total # of pieces of a team equals # in a contiguous bunch
        whiteWon = numWhite == self.board.findConnectedPieceSize("white")
        blackWon = numBlack == self.board.findConnectedPieceSize("black")
        
        #win states
        if whiteWon and blackWon:
            print("Tie")
            return True
        elif whiteWon:
            print("white wins")
            return True
        elif blackWon:
            print("black wins")
            return True
        
        return False

    def play(self):
        #returns True if there has been a click since last time function was called
        isClick = stddraw.mousePressed()

        #condition from picking -> moving
        if isClick and self.selected != None: #if there's a click and something has already been selected
            self.state = "moving"
        #condition from idle -> picking
        elif isClick:
            self.state = "picking"

        print(self.state)

        #displays the current game state
        self.display()

        if self.won():
            quit()
        

if __name__ == "__main__":
    game = LinesOfAction(SIZE)
    while True:
        game.play()