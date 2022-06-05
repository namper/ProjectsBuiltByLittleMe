import random
import pygame

class Cell(pygame.sprite.Sprite):
    bomb = None
    def __init__(self, i, j, has_bomb, group):
        if self.bomb is None:
            Cell.bomb = pygame.image.load('bomb.png')
            Cell.cover = pygame.image.load('cover.png')
            Cell.font = pygame.font.Font('freesansbold.ttf',15)
        self.i, self.j = i, j
        self.has_bomb = has_bomb
        self.image = self.cover
        self.rect = self.image.get_rect()
        self.rect.topleft = (i*16, j*16)
        super(Cell, self).__init__(group)

    def uncover(self, board):
        if self.has_bomb:
            self.image = self.bomb
        else:
            num = board.count(self)
            if num:
                self.image = self.font.render(str(num), True, (0, 0, 0))
                self.rect = self.image.get_rect()
                self.rect.center = (self.i*16+8, self.j*16+8)
            else:
                self.kill()
                del board.cells[self.i, self.j]

class Board(pygame.sprite.Group):
    def __init__(self, size, chance=.2):
        super(Board, self).__init__()
        self.size = size
        self.cells = {}
        for i in range(size):
            for j in range(size):
                self.cells[i, j] = Cell(i, j, random.random()<chance, self)

    def count(self, cell):
        '''Count the number of bombs near the cell.'''
        return sum(self.cells[i, j].has_bomb
            for i in range(max(0, cell.i-1), min(self.size, cell.i+2))
                for j in range(max(0, cell.j-1), min(self.size, cell.j+2))
                    if (i, j) in self.cells)

class Game(object):
    def main(self, screen):
        board = Board(20)

        screen.fill((255, 255, 255))
        board.draw(screen)
        pygame.display.update()

        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                i = x // 16
                j = y // 16
                if (i, j) not in board.cells:
                    continue
                cell = board.cells[i, j]
                cell.uncover(board)
                screen.fill((255, 255, 255))
                board.draw(screen)
                pygame.display.update()
                if cell.has_bomb:
                    break
                    return

        print('GAME OVER')
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                return

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((320, 320))
    Game().main(screen)
