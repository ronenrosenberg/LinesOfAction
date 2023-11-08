import Board
import Piece
import stddraw


SIZE = 10

class LinesOfAction:
    def __init__(self, SIZE = 10):
        self.board = Board(SIZE)
        self.SIZE = SIZE

    def display(self):
        stddraw.clear()

        #a few definitions
        size = self.SIZE
        side = 1.0/size
        half = side/2.0

        #draw the board
        for x in range(size):
            for y in range(size):
                square = self.board.getBoard()[x , y]
                if (square != None):
                    stddraw.setPenColor(stddraw.RED)
                    stddraw.filledCircle(x*side + half, y*side + half, half/0.5*0.3)
                    stddraw.setPenColor(stddraw.BLACK)
                else:
                    stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
                    stddraw.filledSquare(x*side + half, y*side + half, half)
                    stddraw.setPenColor(stddraw.BLACK)
                stddraw.square(x*side + half, y*side + half, half)
        stddraw.show(0)
    
    def play(self):
        self.display()



if __name__ == "__main__":
    game = LinesOfAction(SIZE)
    game.play()