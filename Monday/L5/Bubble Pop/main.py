import pygame
from click import key_handle

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# 1) Download the images, and display one of the images on 
# the screen.

# 2) Create a sprite class called Ball that 
# draws the images given earlier at a location. 
# HINTS: 
# https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
# https://www.geeksforgeeks.org/python/pygame-creating-sprites/


class Ball (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # CHALLENGE: How can we draw different colours
        # of balls?
        self.image = pygame.image.load("Bubble Pop\images\sphere-07.png")
        self.rect = self.image.get_rect()


# 3) Create rows and columns of balls. Store all the balls
# inside of a Group. HINT: Sprite - Group

def main():
    x = Ball()
    while running:
        
        key_handle()
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE
        screen.blit(x.image, x.rect)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    main()