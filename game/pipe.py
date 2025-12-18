import pygame
import random
from config import PIPE_GAP, PIPE_SPEED, PIPE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, 400)

    def update(self):
        self.x -= PIPE_SPEED
        if self.x < -PIPE_WIDTH:
            self.x = SCREEN_WIDTH
            self.height = random.randint(100,400)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT))
        