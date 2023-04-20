import pygame
from sys import exit

pygame.init()

# making width and height variables for later
w = 800
h = 400

# making the window
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('My Game!')
# setting frame rate pt. 1
clock = pygame.time.Clock()
# creatig the surface and making it red
test_surface = pygame.image.load(graphics)


# making a while loop to keep the window open
while True:
    # making an event (for) loop so the user can close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # placing the surface on the window
    # w/2 and sets the surface to the exact middle, this is why I set integers for the (width, height)
    screen.blit(test_surface, (w/2,0))
    
    
    pygame.display.update()
    # setting frame rate pt. 2 
    clock.tick(60)
