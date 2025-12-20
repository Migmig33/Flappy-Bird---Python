import pygame
from pygame.locals import *
from config import *
from game.bird import Bird

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird - Python')

scroll = SCROLL
scroll_speed = SCROLL_SPEED

#get images
bg = pygame.image.load('assets/images/bgImg.png')
ground = pygame.image.load('assets/images/ground.png')



bird_group = pygame.sprite.Group()

flappy = Bird(100, int(SCREEN_HEIGHT / 2))

bird_group.add(flappy)

bird_group = pygame.sprite.Group()

flappy = Bird(100, int(SCREEN_HEIGHT / 2))

bird_group.add(flappy)

run = True
while run:

    clock.tick(FPS)

    #RENDER BACKGROUND
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update()

    #RENDER GROUND, AND SCROLL
    screen.blit(ground, (scroll, 468))
    scroll -= scroll_speed

    if abs(scroll) > 35:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()