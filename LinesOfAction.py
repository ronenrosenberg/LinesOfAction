from Board import *
from Piece import *
import stddraw

SIZE = 10

class LinesOfAction:
    def __init__(self, SIZE = 10):
        self.board = Board(SIZE)
        self.SIZE = SIZE
        self.SIDE = 1.0/SIZE
        self.HALF = self.SIDE/2.0
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
                    #draw black piece
                    else:
                        stddraw.setPenColor(stddraw.BLACK)
                        stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                #draw black borders
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.square(x*side + half, y*side + half, half)
                
        #as long as state isn't idle, will grab click location
        if state != "idle":
            x = round((stddraw.mouseX() - half)/side)
            y = round((stddraw.mouseY() - half)/side)
        if state == "picking":
            #highlights the currently picked piece (given a piece is being clicked)
            highlighted = self.board.getBoard()[x][y]
            if  highlighted != None:
                stddraw.setPenColor(stddraw.YELLOW)
                stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.5)
                #draw white piece
                if highlighted.getTeam() == "white":
                    stddraw.setPenColor(stddraw.WHITE)
                    stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
                #draw black piece
                else:
                    stddraw.setPenColor(stddraw.BLACK)
                    stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)

                self.selected = self.board.getBoard()[x][y]
        if state == "moving":
            self.board.move(self.selected, (x, y))
            self.selected = None
            self.state = "idle"
        
        #don't question this line, it just makes it work
        stddraw.show(0)
    
    def play(self):
        #returns True if there has been a click since last time function was called
        isClick = stddraw.mousePressed()

        #condition from picking -> moving
        if isClick and self.selected != None:
            self.state = "moving"
        #condition from idle -> picking
        elif isClick:
            self.state = "picking"


        print(self.state)
        self.display(self.state)
        



if __name__ == "__main__":
    game = LinesOfAction(SIZE)
    while True:
        game.play()