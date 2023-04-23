import pygame
from sys import exit

pygame.init()

w = 800
h = 400

clock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Pygame 1.0.0')
font = pygame.font.Font('font/Pixeltype.ttf', 50)
sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()
snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom = (600,300))
player = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_rect = player.get_rect(midbottom = (200,300))
score = font.render('Score:', False, (64,64,64))
score_rect = score.get_rect(center = (w/2,50))

snail_x = 600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    fps = str(int(clock.get_fps()))
    fps_counter = font.render(fps, False, 'Black')
    
    # sky
    screen.blit(sky, (0, 0))
    # ground
    screen.blit(ground, (0, 300))
    # drawing
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    pygame.draw.line(screen, (0,0,255), (0,0), (pygame.mouse.get_pos()),10)
    pygame.draw.ellipse(screen, (0,0,255), pygame.Rect(50, 200, 100, 100))
    # score 
    screen.blit(score, (score_rect))
    # fps counter
    screen.blit(fps_counter, (10, 10))
    # player
    screen.blit(player, (player_rect))
    
    
    
    
    
    
    
    
    
    
    
    
    
    pygame.display.update()
    clock.tick(60)