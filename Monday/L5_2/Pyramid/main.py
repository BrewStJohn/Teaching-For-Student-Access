# Example file showing a basic pygame "game loop"
import pygame
from card import Card

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
running = True

# 1) Create a Card and draw it to the screen
# HINT: image.load, Surface (get rect, blit), Rect 

# ace_of_spades = pygame.image.load("Pyramid\\images\\Spades 1.png")
# ace_rect = ace_of_spades.get_rect()
# ace_rect.center = (360, 240)



# 2e) Create an instance of this class in your main
# game loop and draw it to the screen
five_hearts = Card("5", "Hearts")
print(five_hearts.rect)

king_diamonds = Card("13", "Diamond")
king_diamonds.rect = (300, 300)

# 3) Design a Deck class
# --> what properties and methods should a deck have?

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    # screen.blit(ace_of_spades, ace_rect)
    screen.blit(five_hearts.image, five_hearts.rect)
    screen.blit(king_diamonds.image, king_diamonds.rect)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()