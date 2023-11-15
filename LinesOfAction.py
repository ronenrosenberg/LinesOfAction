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

    def display(self, state):
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
        if state != "idle":
            x = round((stddraw.mouseX() - half)/side)
            y = round((stddraw.mouseY() - half)/side)
        #state activated when there's been a click
        if state == "picking":
            highlighted = self.board.getBoard()[x][y]
            if  highlighted != None: #makes sure that clicked square has a piece in it
                #highlights piece
                stddraw.setPenColor(stddraw.YELLOW)
                stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.5)
                #draw white piece
                if highlighted.getTeam() == "white":
                    stddraw.setPenColor(stddraw.WHITE)
                    stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                else: #otherwise draw the black piece
                    stddraw.setPenColor(stddraw.BLACK)
                    stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                
                #piece is "selected"
                self.selected = self.board.getBoard()[x][y]
            else: #if no piece has been selected, go back to idle
                self.state = "idle"

                
        #state activated on a second click, to move the piece to the second click
        if state == "moving":
            self.board.move(self.selected, (x, y))
            self.selected = None

            #reset state
            self.state = "idle"
        
        #don't question this line, it just makes it work
        stddraw.show(0)
    
    #checks for win state
    def won(self):
        #might be better to put into Board
        print(self.board.teamTotalPieces())
        """
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                if numBlack == self.board.numCol(Piece("white", (x, y))): return True
                """
        

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
        self.display(self.state)

        if self.won():
            quit()
        



if __name__ == "__main__":
    game = LinesOfAction(SIZE)
    while True:
        game.play()