# Example file showing a basic pygame "game loop"
import pygame
from ball import Ball

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 700))
clock = pygame.time.Clock()
running = True

# 1) Draw a ball to the screen
# HINT: Display images with Pygame
# Copy Relative Path: Bubble Pop\images\sphere-05.png
# --> be sure to download the images linked in the chat

# How can we make more than one ball?
# ball1 = Ball((0,0),"Bubble Pop\images\sphere-11.png")
balls = pygame.sprite.Group()

for i in range(11):
    balls.add(Ball((i*50,0), "Bubble Pop\images\sphere-11.png"))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    # screen.blit(ball1.image, ball1.rect)
    balls.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # 4) print to the terminal whenever you press
    # the left and right keys

    clock.tick(60)  # limits FPS to 60

pygame.quit()

