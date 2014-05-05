import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500), 0, 32)
mainClock = pygame.time.Clock()

screen.lock()
circleRect = pygame.draw.circle(screen, (255, 255, 255), (100, 200), 40)
screen.unlock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    circleRect.top += 1

    pygame.display.update()
    mainClock.tick(40)
