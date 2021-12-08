import numpy as np


class Board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0, 1, 0],
                      [1, 0, 0, 1, 1, 0, 0],
                      [2, 2, 0, 1, 0, 0, 0],
                      [2, 1, 1, 2, 0, 0, 0],
                      [1, 0, 2, 1, 2, 0, 0]]

    def reset(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

    def drop_piece(self, player_num, col):
        """Return true if piece was able to be dropped in desired column"""
        if self.board[0][col] == 0:
            for i in range(6):
                if self.board[5-i][col] == 0:
                    self.board[5 - i][col] = player_num
                    break
            return True
        else:
            return False

    def check_win(self):
        # check rows
        for row in self.board:
            for i in range(4):
                if len(set(row[i:i+4])) == 1 and row[i] != 0:
                    print("win by row")
                    return row[i]

        # check columns
        temp = self.board.copy()
        temp = np.array(temp)
        temp = temp.transpose()
        for row in temp:
            for i in range(3):
                if len(set(row[i:i+4])) == 1 and row[i] != 0:
                    print("win by column")
                    return row[i]

        # check diagonal
        temp = self.board.copy()
        temp = np.array(temp)
        # 3 for row shift, 4 for col
        for i in range(3):
            temp_rows = temp[i:i + 4]
            for j in range(4):
                square = [r[j:j+4] for r in temp_rows]
                square = np.array(square)
                if len(set(square.diagonal())) == 1 and square[0][0] != 0:
                    return square[0][0]
                elif len(set(np.fliplr(square).diagonal())) == 1 and square[0][3] != 0:
                    return square[0][3]

    def print(self):
        for row in self.board:
            print(row)


if __name__ == "__main__":
    board = Board()
    # board.reset()

    while True:
        #board.drop_piece(1, col)
        board.print()

        print(board.check_win())
        col = int(input())
