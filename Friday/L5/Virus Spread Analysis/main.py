import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((850, 480))
pygame.display.set_caption("Virus Spread Analysis")
running = True

# other global vars
font = pygame.font.SysFont(None, 70)
viruses = pygame.sprite.Group()
doctors = pygame.sprite.Group()
doc_num = 1
bac_num = 5
split_time = 250
clock = pygame.time.Clock()







# CHALLENGE: Add the doctor and virus classes to their own file as modules.
class Virus(pygame.sprite.Sprite):
    def __init__(self, pos, split_time):
        super().__init__()

        # image, very common way to create a Surface
        self.image = pygame.image.load('Virus Spread Analysis\\virus.png')
        self.image = pygame.transform.smoothscale(self.image, (15, 15))

        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Speed
        self.speed = pygame.math.Vector2(0,5)
        self.speed.rotate_ip(random.randint(0, 360))

        # Virus Duplication
        self.time = 0 # how much time has passed 
        self.split_time = split_time # how many seconds should pass before the
        # virus will split

    def update(self):
        # how do I get this guy to move around?
        self.rect = self.rect.move(self.speed)
        # the sprite doesnt move irradically. How?
        # --> try rotating the vector periodically

        # this code below is close, but needs some work
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

        # how can we get viruses to duplicate?
        # NOTE: How often should the viruses duplicate?
        # HINT: Create a new virus at the same location as this virus
        # HINT: pygame.sprite.Sprite.groups()

        # how do we keep track of how much time has passed?
        # once the time has passed, duplicate the virus?
        self.groups().add() #add a new virus













def main():
    # Game loop
    global running
    testDoctor = Virus((300,300))
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        text = font.render(f"Virus Count: {len(viruses)}", True, (255, 0, 0))
        text_rect = text.get_rect()

        screen.fill((26, 255, 255))
        screen.blit(text, text_rect)
        screen.blit(testDoctor.image, testDoctor.rect)

        pygame.display.flip()


if __name__ == "__main__":
    main()