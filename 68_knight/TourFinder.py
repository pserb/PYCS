from time import sleep


class TourFinder:
    board = []
    sideLength = 0
    solved = False

    def __init__(self, n):
        self.sideLength = n
        self.board = [ [0]*(n+4) for i in range(n + 4)]

        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if (row <= 1) or (row >= len(self.board) - 2) or (col <= 1) or (col >= len(self.board) -2):
                    self.board[row][col] = -1
                else:
                    self.board[row][col] = 0

    def __str__(self):
        retStr = '\033c'
        
        for i in range(self.sideLength + 4):
            for j in range(self.sideLength + 4):
                retStr = retStr + "%3d" % self.board[j][i]
            retStr = retStr + "\n"
        return retStr

    def findTour(self, x, y, moves):
        if (self.solved):
            quit()
        if (moves == self.sideLength * self.sideLength + 1):
            self.solved = True
            print(self)
            return
        if (self.board[x][y] != 0):
            return
        else:
            self.board[x][y] = moves
            print(self)
            # sleep(0.1)

            self.findTour(x+1, y+2, moves+1)
            self.findTour(x+2, y+1, moves+1)
            self.findTour(x+2, y-1, moves+1)
            self.findTour(x+1, y-2, moves+1)
            self.findTour(x-1, y-2, moves+1)
            self.findTour(x-2, y-1, moves+1)
            self.findTour(x-2, y+1, moves+1)
            self.findTour(x-1, y+2, moves+1)

            self.board[x][y] = 0
            print(self)


b = TourFinder(6)
b.findTour(2, 2, 1)
# print(b)