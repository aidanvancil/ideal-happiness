# Imports
from shut_the_box.constants import SIZE, TAN, BROWN
from shut_the_box.game import Game 
import pygame

# Display
WINDOW = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Shut The Box')
FPS = 60

def get_pos():
    x, y = pygame.mouse.get_pos()
    return (x, y)

def check_pos(selected_area):
    areas = Game.get_areas()
    checked_areas = []
    for area in areas:
        if selected_area[0] >= area[0][0] and selected_area[0] <= area[1][0]:
            if selected_area[1] >= area[0][1] and selected_area[1] <= area[1][1]:
                checked_areas.append(True)
        checked_areas.append(False)
    return checked_areas

def main():
    game = Game(WINDOW)
    running = True
    clock = pygame.time.Clock()
    WINDOW.fill(TAN)
    while running:
        update_mark = True
        clock.tick(FPS)
        if (game.win()):
            YouWin = pygame.transform.scale(pygame.image.load(r'.\assets\YouWin.png'), (500, 150))
            WINDOW.blit(YouWin, (100, 300))
            pygame.display.flip()
            pygame.time.wait(5000)
            print("You Won, Congrats")
            break
        if (game.loss()):
                YouLost = pygame.transform.scale(pygame.image.load(r'.\assets\YouLost.png'), (500, 150))
                WINDOW.blit(YouLost, (100, 300))
                pygame.display.flip()
                pygame.time.wait(5000)
                print("You Lost, Lame")
                break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.draw.circle(WINDOW, BROWN, (50, 400), 40).collidepoint(pygame.mouse.get_pos()) and game.board.remaining == 0:
                    game.get_roll_before()
                selected_area = get_pos()
                checked_areas = check_pos(selected_area)
                if any(checked_areas):
                    domino_selected = "".join(str([i for i, trues in enumerate(checked_areas) if trues]))
                    domino_selected = int(domino_selected[1]) + 1
                    if domino_selected in game.board.pieces and domino_selected <= game.board.remaining:
                        game.update(domino_selected)
                        update_mark = False
        if update_mark:
            game.update(0)
    pygame.quit()
                
if __name__ == '__main__':
    main()