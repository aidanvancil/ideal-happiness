# IMPORTS
import pygame
from .constants import TAN, BROWN, BLACK, DOMINO_SIZE
from .domino import Domino
import random

class Board():
    # Constructors
    def __init__(self):
        self.rolldice = pygame.image.load(r'.\assets\RollDice.png')
        self.totalphrase = pygame.image.load(r'.\assets\TotalPhrase.png')
        self.domino = Domino()
        self.remaining = 0
        self.after_first = False
        self.pieces = [0,1,2,3,4,5,6,7,8,9]
        
        
    def draw_dice_roll(self):
        if sum(self.pieces) <= 6:
            total = (random.randint(1,6), 0)
            return total
        total = (random.randint(1,6), random.randint(1,6))
        return total
    
    def draw(self, window, domino_selected):
        pygame.draw.circle(window, TAN, (310, 450), 80)
        pygame.draw.circle(window, BLACK, (55, 403), 47)
        pygame.draw.circle(window, BROWN, (55, 403), 45)
        window.blit(self.rolldice, (0, 380))
        window.blit(self.totalphrase, (100, 450))
        
        #Get Remaining Count
        if self.remaining > 0:
            self.after_first = True

        if self.remaining == 0 and self.after_first:
            window.blit(self.rolldice, (280, 450))
        if self.remaining == 1:
            window.blit(self.domino.num1, (280, 440))
        elif self.remaining == 2:
            window.blit(self.domino.num2, (280, 440))
        elif self.remaining == 3:
            window.blit(self.domino.num3, (280, 440))
        elif self.remaining == 4:
            window.blit(self.domino.num4, (280, 440))
        elif self.remaining == 5:
            window.blit(self.domino.num5, (280, 440))
        elif self.remaining == 6:
            window.blit(self.domino.num6, (280, 440))
        elif self.remaining == 7:
            window.blit(self.domino.num7, (280, 440))
        elif self.remaining == 8:
            window.blit(self.domino.num8, (280, 440))
        elif self.remaining == 9:
            window.blit(self.domino.num9, (280, 440))
        elif self.remaining == 10:
            window.blit(self.domino.num10, (280, 440))
        elif self.remaining == 11:
            window.blit(self.domino.num11, (280, 440))
        elif self.remaining == 12:
            window.blit(self.domino.num12, (280, 440))

        if domino_selected in self.pieces:
            self.remaining -= domino_selected
            self.pieces.remove(domino_selected)

        # Build Pieces Thru Images
        for i in range(9):
            if domino_selected  == 0:
                pygame.draw.rect(window, BLACK, (i*DOMINO_SIZE + 18, 10, DOMINO_SIZE//2 + 5, DOMINO_SIZE + 5)) 
                pygame.draw.rect(window, BROWN, (i*DOMINO_SIZE + 20, 12, DOMINO_SIZE//2, DOMINO_SIZE))
            if i+1 in self.pieces:
                pygame.draw.rect(window, BLACK, (i*DOMINO_SIZE + 18, 10, DOMINO_SIZE//2 + 5, DOMINO_SIZE + 5)) 
                pygame.draw.rect(window, BROWN, (i*DOMINO_SIZE + 20, 12, DOMINO_SIZE//2, DOMINO_SIZE))

            if i == 0 and 1 in self.pieces:
                window.blit(self.domino.num1, (i*DOMINO_SIZE + 18, 40))
            elif i == 1 and 2 in self.pieces:
                window.blit(self.domino.num2, (i*DOMINO_SIZE + 18, 40))
            elif i == 2 and 3 in self.pieces:
                window.blit(self.domino.num3, (i*DOMINO_SIZE + 18, 40))
            elif i == 3 and 4 in self.pieces:
                window.blit(self.domino.num4, (i*DOMINO_SIZE + 18, 40))
            elif i == 4 and 5 in self.pieces:
                window.blit(self.domino.num5, (i*DOMINO_SIZE + 18, 40))
            elif i == 5 and 6 in self.pieces:
                window.blit(self.domino.num6, (i*DOMINO_SIZE + 18, 40))
            elif i == 6 and 7 in self.pieces:
                window.blit(self.domino.num7, (i*DOMINO_SIZE + 18, 40))
            elif i == 7 and 8 in self.pieces:
                window.blit(self.domino.num8, (i*DOMINO_SIZE + 18, 40))
            elif i == 8 and 9 in self.pieces:
                window.blit(self.domino.num9, (i*DOMINO_SIZE + 18, 40))
           