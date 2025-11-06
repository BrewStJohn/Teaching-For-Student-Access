# 1) Create and run the basic tutorial from the 
# Pygame documentation

# 2) Take a look at the pygame tutorial in the chat. Your next 
# objective is to create a ball on the screen.
# BONUS: Make the ball move around on the screen, reflecting off the
# edges.

# 3) Create a class called "Ball"
# and create 3 objects from the class and draw those to the screen.
# HINT: OOP, Sprite

# 4) Investigate how to create a ball when you click on the screen.
# HINT: Mouse

# Example file showing a basic pygame "game loop"
import pygame, random

# pygame setup
pygame.init()
height, width = (1280, 720)
screen = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()
running = True
speed = [10, -2]

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = [random.randint(-5, 5), random.randint(-5, 5)]
        self.size = random.uniform(0.05, 0.3)
        self.image = pygame.image.load("Intro Pygame/ball.jpg")
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(200, width-200),random.randint(200, height-200))

    def update(self):
        if self.rect.left < 0 or self.rect.right > height:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > width:
            self.speed[1] = -self.speed[1]

testBall = Ball()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    testBall.update()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    screen.blit(testBall.image, testBall.rect)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()