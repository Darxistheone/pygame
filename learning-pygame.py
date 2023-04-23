import pygame
from sys import exit

pygame.init()

# making width and height variables for later
w = 800
h = 400

# making the window
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('My Game!')
# setting frame rate pt. 1
clock = pygame.time.Clock()
# create the font
font = pygame.font.Font('font/Pixeltype.ttf', 50)
# creatig the surface and making it red
sky = pygame.image.load('graphics/Sky.png').convert()
ground = pygame.image.load('graphics/ground.png').convert()
snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom = (600,300))
player = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_gravity = 0
player_rect = player.get_rect(midbottom = (200,300))
score = font.render('Score:', False, (64,64,64))
score_rect = score.get_rect(center = (w/2,50))


# making a pos for snail_x
snail_x = 600

# making a while loop to keep the window open
while True:
    # making an event (for) loop so the user can close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            player_gravity = -20
    #if event.type == pygame.MOUSEMOTION:
    #    print(event.pos)
    
    #if event.type == pygame.MOUSEBUTTONDOWN:
    #    print('Mouse Clicked!')
    
    # sees if the mouse collides with the player
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint((mouse_pos)):
        print('Mouse Colided!')
    
    # fps counter
    fps = str(int(clock.get_fps()))
    fps_counter = font.render(fps, False, 'Black')
    
    
    
    # placing the surface on the window
    # w/2 and sets the surface to the exact middle, this is why I set integers for the (width, height)
    # the order of the blit matters because right now if the ground was at (0,0), it would cover the sky because it is being displayed after or over it
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
    player_gravity += 1
    screen.blit(player, (player_rect))
    player_rect.y += player_gravity
    
    
    # making an animation of the snail crossing the screen on loop
    snail_rect.left -= 4
    if snail_rect.left == -100:
        snail_rect.left = 800
    screen.blit(snail,(snail_rect))
    
    # checking if the snail collides with the player
    # if snail_rect.colliderect(player_rect):
    #    print('Collision Detected!')
    
    # finds the keys pressed on the mouse while over the player
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #    print(pygame.mouse.get_pressed())
    
    pygame.display.update()
    # setting frame rate pt. 2
    clock.tick(60)
