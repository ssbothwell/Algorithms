#!/usr/bin/env python

class board:
    def __init__(self, rows=10, cols=10):
        self.cols = cols
        self.rows = rows
        self.matrix = [[0] * rows for _ in range(cols)]

    def set(self, row, col, val):
        self.matrix[row][col] = val

    def get(row, col, val):
        return self.matrix[row][col]

    def check_neighbors(self, row, col):

        def check_n():
            if row > 0:
                return self.matrix[row-1][col]
            else:
                return 0

        def check_nw():
            if row > 0 and col > 0:
                return self.matrix[row-1][col-1]
            else:
                return 0

        def check_ne():
            if row != self.rows - 1 and col != self.cols - 1:
                return self.matrix[row-1][col+1]
            else:
                return 0

        def check_e():
            if col != self.rows - 1:
                return self.matrix[row][col+1]
            else:
                return 0

        def check_w():
            if col > 0:
                return self.matrix[row][col-1]
            else:
                return 0

        def check_s():
            if row != self.rows - 1:
                return self.matrix[row+1][col]
            else:
                return 0

        def check_sw():
            if row != self.rows - 1 and col > 0:
                return self.matrix[row+1][col-1]
            else:
                return 0

        def check_se():
            if row != self.rows -1 and col != self.cols -1:
                return self.matrix[row+1][col+1]
            else:
                return 0

        return check_n()+check_ne()+check_nw()+check_e()+check_w()+check_s()+check_se()+check_sw()

    def update(self):
        new_matrix = [[0] * self.rows for _ in range(self.cols)]

        for i, row in enumerate(self.matrix):
            for j, col in enumerate(row):
                score = self.check_neighbors(i,j)
                if col == 1:
                    if score >= 2 and score < 4:
                        new_matrix[i][j] = 1
                    else:
                        new_matrix[i][j] = 0
                elif col == 0 and score == 3:
                    new_matrix[i][j] = 1
        self.matrix = new_matrix

    def print(self):
        for row in self.matrix:
            print(row)
        print()


if __name__ == '__main__':
    game = board(6,6)
    game.matrix =   [[0,0,0,0,0,0]
                    ,[0,0,0,0,0,0]
                    ,[0,0,1,1,1,0]
                    ,[0,1,1,1,0,0]
                    ,[0,0,0,0,0,0]
                    ,[0,0,0,0,0,0]
                    ]
    game.print()
    game.update()
    game.print()
    game.update()
    game.print()
    game.update()
    game.print()
