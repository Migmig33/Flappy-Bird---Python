import pygame
from pygame.locals import *
from config import *
from game.bird import Bird
from game.pipe import Pipe
from game.button import Button
import random

pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird - Python')

#game config
score = 0
bird_passed = False
scroll = SCROLL
scroll_speed = SCROLL_SPEED
pipe_frequency = PIPE_FREQ

last_pipe = pygame.time.get_ticks() - pipe_frequency


# LOAD MUSIC 
score_sound = pygame.mixer.Sound('assets/sounds/score.mp3')
game_over = pygame.mixer.Sound('assets/sounds/game_over.mp3')
game_over.set_volume(0.8)
bgm = pygame.mixer.Sound('assets/sounds/bgm.mp3')
bgm.set_volume(0.5)
bgm.play(1)
# LOAD IMAGES
bg = pygame.image.load('assets/images/bgImg.png')
ground = pygame.image.load('assets/images/ground.png')



bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
restart_button = pygame.sprite.Group()
flappy = Bird(100, int(SCREEN_HEIGHT / 2))
bird_group.add(flappy)

button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 100, restart_button)



# RENDER TEXT ON SCREEN FUNCTION
fontNormal = pygame.font.SysFont('Bauhaus 93', 60)
fontSmall = pygame.font.SysFont('Bauhaus 93', 20)
white = (255,255,255)
def draw_text(text, font, text_col, x, y, shadow = True, shadow_offset = 3, center = False):

    if center: 
        text_width = font.render(text, True, text_col).get_width()
        x = x - text_width // 2
    if shadow:
        shadow_img = font.render(text, True, (0,0,0))
        screen.blit(shadow_img, (x + shadow_offset, y + shadow_offset))


    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def start_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(SCREEN_HEIGHT / 2)
    score = 0
    return score

run = True
while run:

    clock.tick(FPS)

    #RENDER BACKGROUND
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update(FLY, GAME_OVER)

    pipe_group.draw(screen)
    pipe_group.update(FLY, GAME_OVER)

    #DRAW GROUND
    screen.blit(ground, (scroll, 468))

    #SCORE CHECKER
    if len(pipe_group) > 0:
        if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
            and bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
            and bird_passed == False:
            bird_passed = True
        if bird_passed == True:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                score_sound.set_volume(1)
                score_sound.play()
                bird_passed = False

    
  
     # RENDER TEXT
    if FLY == False and GAME_OVER == False:
        draw_text(str('Flappy Bird'), fontNormal, white, int(SCREEN_WIDTH / 2), 40, center = True)
        draw_text(str('Click Any Where To Start'), fontSmall, white, int(SCREEN_WIDTH / 2), 350, center= True)
    if FLY == True and GAME_OVER == False:
        #RENDER SCORE AFTER START
        draw_text(str(score), fontNormal, white, int(SCREEN_WIDTH / 2), 20, center= True)



    game_over_trigger = False
    #GAME_OVER IF:
    #IF BIRD COLLIDE TO THE PIPE OR FLY TOO HIGH
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False)  or flappy.rect.top < 0:
        game_over_trigger = True
        
       

    #IF BIRD HIT THE GROUND
    if flappy.rect.bottom >= 460:
        game_over_trigger = True
        FLY = False
        
    if game_over_trigger and GAME_OVER == False:
        game_over.play()
        GAME_OVER = True
    if GAME_OVER == True:
        draw_text(str('Game Over'), fontNormal, white, int(SCREEN_WIDTH / 2), 20, center= True)
        draw_text(str(f'Your Score is: {score}'), fontSmall, white, int(SCREEN_WIDTH / 2), 80, center= True)
        if button.draw() == True:
            GAME_OVER = False
            score = start_game()
            


    
    if GAME_OVER == False and FLY == True:

        #GENERATE PIPES
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-50, 50)
            btm_pipe = Pipe(500, int(SCREEN_HEIGHT / 2) + pipe_height, -1)
            top_pipe = Pipe(500, int(SCREEN_HEIGHT / 2) + pipe_height, 1)
            pipe_group.add(btm_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

    if GAME_OVER == False:
            
        #RENDER GROUND, AND SCROLL
        scroll -= scroll_speed
        if abs(scroll) > 35:
            scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and FLY == False:
            FLY = True

    pygame.display.update()

  
pygame.quit()