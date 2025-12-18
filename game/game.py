import pygame
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS
from game.bird import Bird
from game.pipe import Pipe
from utils.loader import BG_IMG
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird - Python")
        self.clock = pygame.time.Clock()

        BG_IMG.convert()

        self.background = pygame.transform.scale(BG_IMG, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.bird = Bird()
        self.pipes = [Pipe()]
        self.score = 0
        self.running = True
    
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.jump()

    def update(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()

            #Check if bird hit the Pipe
            bird_rect = pygame.Rect(self.bird.x - self.bird.radius, self.bird.y - self.bird.radius,
                                    self.bird.radius*2, self.bird.radius*2)
            top_pipe = pygame.Rect(pipe.x, 0, 50, pipe.height)
            bottom_pipe = pygame.Rect(pipe.y, pipe.height + 150, 50, SCREEN_HEIGHT)
            if bird_rect.collidedict(top_pipe) or bird_rect.collidedict(bottom_pipe):
                self.running = False
            
        # Check if bird hit ceiling or ground
        if self.bird.y > SCREEN_HEIGHT or  self.bird.y < 0:
            self.running = False

    def draw(self):
        self.screen.blit(self.background, (0,0))
        for pipe in self.pipe:
            pipe.draw(self.screen)

            self.bird.draw(self.screen)
            font = pygame.font.SysFont(None, 36)
            text = font.render(f"Game Over: Score: {self.score}", True, (0,0,0))
            self.screen.blit(text, (10,10))

            pygame.display.update()