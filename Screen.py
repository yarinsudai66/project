import pygame

size = (600, 400)
screen = pygame.display.set_mode(size)
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

    screen.fill((255, 255, 255))
    pygame.display.update()