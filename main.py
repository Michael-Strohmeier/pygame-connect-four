import pygame
import numpy as np

global BLACK
global WHITE
global GREEN
global RED
global BLUE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Game:
    def __init__(self):
        self.player_num = 1
        self.board = None
        self.winner = 0
        self.reset()

    def reset(self):
        self.player_num = 1
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

    def drop_piece(self, col):
        """Return true if piece was able to be dropped in desired column"""
        if self.board[0][col] == 0:
            for i in range(6):
                if self.board[5-i][col] == 0:
                    self.board[5 - i][col] = self.player_num
                    break

            if self.player_num == 1:
                self.player_num = 2
            else:
                self.player_num = 1

            return True
        else:
            return False

    def check_win(self):
        # check tie
        if 0 not in self.board[0]:
            return 0

        # check rows
        for row in self.board:
            for i in range(4):
                if len(set(row[i:i+4])) == 1 and row[i] != 0:
                    return row[i]

        # check columns
        temp = self.board.copy()
        temp = np.array(temp)
        temp = temp.transpose()
        for row in temp:
            for i in range(3):
                if len(set(row[i:i+4])) == 1 and row[i] != 0:
                    return row[i]

        # check diagonal
        temp = self.board.copy()
        temp = np.array(temp)
        for i in range(3):
            temp_rows = temp[i:i + 4]
            for j in range(4):
                square = [r[j:j+4] for r in temp_rows]
                square = np.array(square)
                if len(set(square.diagonal())) == 1 and square[0][0] != 0:
                    return square[0][0]
                elif len(set(np.fliplr(square).diagonal())) == 1 and square[0][3] != 0:
                    return square[0][3]

        return None

    def print(self):
        for row in self.board:
            print(row)

    def draw(self, screen):
        for i, row in enumerate(self.board):
            for j, e in enumerate(row):
                x = j * 100 + 50
                y = i * 100 + 50
                c = WHITE

                if e == 1:
                    c = BLUE
                elif e == 2:
                    c = RED

                pygame.draw.circle(screen, c, (x, y), 30)

    def display_winner(self, screen, pygame_font):
        winner = self.check_win()
        label = None
        if winner == 1:
            label = pygame_font.render("Player 1 wins!!", 1, BLUE)
        elif winner == 2:
            label = pygame_font.render("Player 2 wins!!", 1, RED)
        elif winner == 0:
            label = pygame_font.render("Tie", 1, BLACK)
        if label:
            screen.blit(label, (40, 10))


def main():
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 600
    FPS = 60  # frame rate

    clock = pygame.time.Clock()
    pygame.init()
    pygame.font.init()

    pygame_font = pygame.font.SysFont('Comic Sans MS', 30)

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    game = Game()

    while main:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == ord("q"):
                    pygame.quit()
                if event.key == ord("r"):
                    game.reset()
                if 49 <= event.key and event.key <= 55 and game.check_win() == None:
                    col = event.key - 49
                    game.drop_piece(col)

        screen.fill((230, 230, 230))

        game.draw(screen)
        game.display_winner(screen, pygame_font)

        # here we should probably check if there is a winner or not and
        # draw player 1 wins or something
        # the return values are
        # 0 = tie
        # 1 = player 1 won
        # 2 = player 2 won
        # None = no one won
        # game.check_win()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
