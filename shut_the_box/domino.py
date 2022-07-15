import pygame

class Domino():
    def __init__(self):
        # Dice(s)
        self.dice1 = pygame.image.load(r'.\assets\dice1.png')
        self.dice1 = pygame.transform.scale(self.dice1, (45, 45))
        self.dice2 = pygame.image.load(r'.\assets\dice2.png')
        self.dice2 = pygame.transform.scale(self.dice2, (45, 45))
        self.dice3 = pygame.image.load(r'.\assets\dice3.png')
        self.dice3 = pygame.transform.scale(self.dice3, (45, 45))
        self.dice4 = pygame.image.load(r'.\assets\dice4.png')
        self.dice4 = pygame.transform.scale(self.dice4, (45, 45))
        self.dice5 = pygame.image.load(r'.\assets\dice5.png')
        self.dice5 = pygame.transform.scale(self.dice5, (45, 45))
        self.dice6 = pygame.image.load(r'.\assets\dice6.png')
        self.dice6 = pygame.transform.scale(self.dice6, (45, 45))

        # Number(s)
        self.num1 = pygame.image.load(r'.\assets\numbers\num1.png')
        self.num1 = pygame.transform.scale(self.num1, (35, 70))
        self.num2 = pygame.image.load(r'.\assets\numbers\num2.png')
        self.num2 = pygame.transform.scale(self.num2, (35, 70))
        self.num3 = pygame.image.load(r'.\assets\numbers\num3.png')
        self.num3 = pygame.transform.scale(self.num3, (35, 70))
        self.num4 = pygame.image.load(r'.\assets\numbers\num4.png')
        self.num4 = pygame.transform.scale(self.num4, (35, 70))
        self.num5 = pygame.image.load(r'.\assets\numbers\num5.png')
        self.num5 = pygame.transform.scale(self.num5, (35, 70))
        self.num6 = pygame.image.load(r'.\assets\numbers\num6.png')
        self.num6 = pygame.transform.scale(self.num6, (35, 70))
        self.num7 = pygame.image.load(r'.\assets\numbers\num7.png')
        self.num7 = pygame.transform.scale(self.num7, (35, 70))
        self.num8 = pygame.image.load(r'.\assets\numbers\num8.png')
        self.num8 = pygame.transform.scale(self.num8, (35, 70))
        self.num9 = pygame.image.load(r'.\assets\numbers\num9.png')
        self.num9 = pygame.transform.scale(self.num9, (35, 70))
        self.num10 = pygame.image.load(r'.\assets\numbers\num10.png')
        self.num10 = pygame.transform.scale(self.num10, (55, 70))
        self.num11 = pygame.image.load(r'.\assets\numbers\num11.png')
        self.num11 = pygame.transform.scale(self.num11, (55, 70))
        self.num12 = pygame.image.load(r'.\assets\numbers\num12.png')
        self.num12 = pygame.transform.scale(self.num12, (55, 70))
    
    # Testing
    def __repr__(self):
        return str(self.pieces)