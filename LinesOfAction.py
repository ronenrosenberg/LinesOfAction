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
                
        if state == "picking":
            xx = stddraw.mouseX()
            yy = stddraw.mouseY()
            x = round((xx - half)/side)
            y = round((yy - half)/side)

            #highlights the currently picked piece
            if self.board.getBoard()[x][y] != None:
                stddraw.setPenColor(stddraw.YELLOW)
                stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.5)
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.4)
        if state == "moving":
            xx = stddraw.mouseX()
            yy = stddraw.mouseY()
            x = round((xx - half)/side)
            y = round((yy - half)/side)

            self.board.getBoard()[x][y] = None
            self.state = "idle"
        #idfk
        stddraw.show(0)
    
    def play(self):
        #condition from picking -> moving
        if stddraw.mousePressed() and self.state == "picking":
            self.state = "moving"
        #condition from idle -> picking
        if stddraw.mousePressed() and self.state == "idle":
            self.state = "picking"

        self.display(self.state)
        



if __name__ == "__main__":
    game = LinesOfAction(SIZE)
    while True:
        game.play()