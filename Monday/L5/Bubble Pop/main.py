import pygame

# 1) Create a blank screen. It can have background.
# 2) Download the images, and display one of the images on 
# the screen.
# 3) Create a sprite class called Ball that 
# draws the images given earlier at a location. 
# HINTS: 
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
# https://www.geeksforgeeks.org/python/pygame-creating-sprites/

# 4) Create rows and columns of balls. Store all the balls
# inside of a Group. HINT: Sprite - Group

class Ball (pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image
        self.rect

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()