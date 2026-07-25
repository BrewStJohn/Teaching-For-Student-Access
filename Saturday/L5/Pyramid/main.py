# 1) Create a pygame application with a green background
# 2) Draw one of the cards to your application
# 3) Create a pygame Sprite class for a card,
# so you can make more than one (card).
# 4) Create a pyramid of cards

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Card(pygame.sprite.Sprite):
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        
        self.image = pygame.image.load(f"Pyramid\PNG\Medium\{self.rank} {self.suite}.png")
        self.rect = self.image.get_rect()

    # CHALLENGE: Create a method called 'flip'
    # that flips the card over to its backside.

# TASK 1: Create cards so they form a pyramid
# TASK 2: Create a new class called Deck
# This class should have 1 property called 
# 'cards' that is a list of 52 Cards.
# HINT: 
# cards_list = []
# for i in range(20):
#     cards_list.append(Card())

# CHALLENGE: Put this class into its own module

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    screen.blit(testCard.image, testCard.rect)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()