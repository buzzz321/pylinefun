import sys, pygame, pygame.gfxdraw, math
pygame.init()

size = width, height = 1200, 1000
speed = [2, 2]
black = 0, 0, 0
colour = (255, 0, 0)

posX = width / 2
posY = height / 2

screen = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.gfxdraw.pixel(screen, int(posX), int(posY), colour)

    posX += speed[0]
    posY += speed[1]

    if posX < 0 or posX > width:
        speed[0] = -speed[0]
    if posY < 0 or posY > height:
        speed[1] = -speed[1]

    #screen.fill(black)
    pygame.display.flip()