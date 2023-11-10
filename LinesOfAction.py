from Board import *
from Piece import *
import stddraw


SIZE = 10

class LinesOfAction:
    def __init__(self, SIZE = 10):
        self.board = Board(SIZE)
        self.SIZE = SIZE

    def display(self):
        """draws a frame of the board"""
        stddraw.clear()

        #a few definitions
        size = self.SIZE
        side = 1.0/size
        half = side/2.0

        #draw the board
        #blue background
        stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
        stddraw.filledSquare(0, 0, 1)
        for x in range(size):
            for y in range(size):
                #get a specifc square of the board
                square = self.board.getBoard()[x][y]
                #if there's a piece on the square
                if (square != None):
                    #draw white piece
                    if square.team == "white":
                        stddraw.setPenColor(stddraw.WHITE)
                        stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.3)
                    #draw black piece
                    else:
                        stddraw.setPenColor(stddraw.BLACK)
                        stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.3)
                #draw black borders
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.square(x*side + half, y*side + half, half)
        #idfk
        stddraw.show(0)
    
    def play(self):
        self.display()



if __name__ == "__main__":
    game = LinesOfAction(SIZE)
    while True:
        game.play()