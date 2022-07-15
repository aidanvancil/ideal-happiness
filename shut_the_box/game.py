from .domino import Domino
from .board import Board
from .constants import DOMINO_SIZE, TAN
import pygame
from itertools import combinations

class Game():    
    def __init__(self, window):
        self._init()
        self.window = window
        self.total =(0,0)
        self.bool = False
    
    def _init(self):
        self.board = Board()
        self.domino = Domino()
    
    def get_roll_before(self):
        total = self.board.draw_dice_roll()
        self.total = total
        self.bool = True
        return total

    def get_roll_after(self):
        total = self.total
        if total[0] == 1:
            self.window.blit(self.domino.dice1, (300, 300))
        elif total[0] == 2:
            self.window.blit(self.domino.dice2, (300, 300))
        elif total[0] == 3:
            self.window.blit(self.domino.dice3, (300, 300))
        elif total[0] == 4:
            self.window.blit(self.domino.dice4, (300, 300))
        elif total[0] == 5:
            self.window.blit(self.domino.dice5, (300, 300))
        elif total[0] == 6:
            self.window.blit(self.domino.dice6, (300, 300))

        if total[1] == 0:
            pygame.draw.circle(self.window, TAN, (385, 325), 40)
        elif total[1] == 1:
            self.window.blit(self.domino.dice1, (350, 300))
        elif total[1] == 2:
            self.window.blit(self.domino.dice2, (350, 300))
        elif total[1] == 3:
            self.window.blit(self.domino.dice3, (350, 300))
        elif total[1] == 4:
            self.window.blit(self.domino.dice4, (350, 300))
        elif total[1] == 5:
            self.window.blit(self.domino.dice5, (350, 300))
        elif total[1] == 6:
            self.window.blit(self.domino.dice6, (350, 300))
        self.bool = False

    def update(self, domino_selected):
        if self.bool:
            self.get_roll_after()
            self.total = str(self.total)
            self.total = ''.join([i for i in self.total if i.isnumeric()])
            remaining = int(self.total[0]) + int(self.total[1])
            self.board.remaining = remaining
            self.board.draw(self.window, domino_selected)
        else:
            self.board.draw(self.window, domino_selected)
        pygame.display.update()

    def win(self):
        if len(self.board.pieces) == 0:
            return True
        return False
    
    def loss(self):
        output = sum([list(map(list, combinations(self.board.pieces, i))) for i in range(len(self.board.pieces) + 1)], [])
        totals = []
        for i in output:
            totals.append(sum(i))
        if self.board.remaining not in totals:
            return True
        return False
    
    @staticmethod
    def get_areas():
        areas = []
        for i in range(9):
            areas.append(((i*DOMINO_SIZE + 18, 10),(DOMINO_SIZE//2 + 5 + (i*DOMINO_SIZE + 18), DOMINO_SIZE + 5 + (10))))
        return areas

    