import pygame

def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10))
    flag = True

    while flag:
        pygame.time.delay(50);
        clock.tick(10);
        redrawWindow(win);