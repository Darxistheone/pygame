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
text = font.render('This Is My Game!', False, 'Black')
snail = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail.get_rect(midbottom = (600,300))


# making a pos for snail_x
snail_x = 600

# making a while loop to keep the window open
while True:
    # making an event (for) loop so the user can close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # fps counter
    fps = str(int(clock.get_fps()))
    fps_counter = font.render(fps, False, 'Black')
    
    
    
    # placing the surface on the window
    # w/2 and sets the surface to the exact middle, this is why I set integers for the (width, height)
    # the order of the blit matters because right now if the ground was at (0,0), it would cover the sky because it is being displayed after or over it
    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))
    screen.blit(text, (w/3, 50))
    screen.blit(fps_counter, (10, 10))
    
    
    # making an animation of the snail crossing the screen on loop
    snail_rect.left -= 4
    if snail_rect.left == -100:
        snail_rect.left = 800
    screen.blit(snail,(snail_rect))
    
    
    
    pygame.display.update()
    # setting frame rate pt. 2
    clock.tick(60)
