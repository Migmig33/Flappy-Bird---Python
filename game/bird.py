import pygame
from config import GRAVITY, JUMP_EFFECT
from utils.loader import BIRD_IMG

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.velocity = 0
        self.image = BIRD_IMG
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
    
    def jump(self):
        self.velocity = JUMP_EFFECT

    
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
    
   