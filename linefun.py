import sys, pygame, pygame.gfxdraw
from math import *

pygame.init()

size = width, height = 1200, 1000
speed = [2, 2]
black = 0, 0, 0
colour = (255, 0, 0)
colour2 = (0, 255, 0)

posX = width / 2
posY = height / 2
pos2X = width / 2
pos2Y = height / 2

pos2X += 30
pos2Y += 30

screen = pygame.display.set_mode(size)

incX = 0
incY = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)

    pygame.gfxdraw.line(screen, int(posX), int(posY), int(pos2X), int(pos2Y),
                        colour)

    posX = posX + sin(radians(incX / 10.0)) * 1.4 * sin(radians(incY / 45.9))
    posY = posY + cos(radians(incY / 10.0)) * 1.4 * sin(radians(incX / 45.0))

    pos2X = pos2X + sin(radians(incX / 5.0)) * 1.2 * sin(radians(incY / 40.9))
    pos2Y = pos2Y + cos(radians(incY / 5.0)) * 1.2 * sin(radians(incX / 40.0))

    incX += speed[0]
    incY += speed[1]

    pygame.display.flip()