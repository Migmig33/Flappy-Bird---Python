import os
import pygame
ASSETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')

BIRD_IMG = pygame.image.load(os.path.join(ASSETS_DIR, 'birdImg.png'))
BOTPIPE_IMG = pygame.image.load(os.path.join(ASSETS_DIR, 'botpipe.png'))
TOPPIPE_IMG = pygame.image.load(os.path.join(ASSETS_DIR, 'toppipe.png'))
BG_IMG = pygame.image.load(os.path.join(ASSETS_DIR, 'bgImg.png'))
