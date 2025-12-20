import pygame
import sys
from pathlib import Path

root = Path(__file__).parent.parent
sys.path.insert(0, str(root))
from config import * 



class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.top_pipe = pygame.image.load('assets/images/botpipe.png')
        self.bot_pipe = pygame.image.load('assets/images/toppipe.png')
        
        if position == 1:
            self.image = self.top_pipe
        if position == -1:
            self.image = self.bot_pipe

        self.rect = self.image.get_rect()
        
        #SET PIPE POSITION
        if position == -1:
            self.rect.bottomleft = [x, y - 60]
        elif position == 1:
            self.rect.topleft = [x, y + 60]

    def update(self, FLY, GAME_OVER):
        if GAME_OVER == False:

            self.rect.x -= SCROLL_SPEED
            if self.rect.right < 0:
                 self.kill()

    
        