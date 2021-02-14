import pygame

def redrawgrid(width, rows, surface):
    sizeBtwn = width//rows

    x = 0
    y = 0
    for i in range(rows):
        x = x + sizeBtw
        y = y + sizeBtwn
        pygame.draw.line(surface, (255, 255, 255), (x.0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, width), (width, y))


