import pygame
import sys
from pathlib import Path

root = Path(__file__).parent.parent
sys.path.insert(0, str(root))
from config import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        self.image = pygame.image.load('assets/images/restart.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        action = False
        
        # GET MOUSE POS
        pos = pygame.mouse.get_pos()

        # CHECK MOUSE IS OVER THE BUTTOn
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        
        #RENDER BUTTON
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

