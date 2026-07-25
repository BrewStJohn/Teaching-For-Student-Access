import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 850
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virus Spread Analysis")
running = True

# other global vars
font = pygame.font.SysFont(None, 70)
viruses = pygame.sprite.Group()
doctors = pygame.sprite.Group()
doc_num = 1
virus_num = 5
split_time = 5
clock = pygame.time.Clock()


# TASK: Create a function called 'init' that initialises
# the game. It should:
# 1) Fill in the Doctors group
# 2) Fill in the Viruses group


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
        self.time += 1
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
        # HINT: once the time has passed, create a new virus 
        # at the same location as this(self) virus 
        # HINT: pygame.sprite.Sprite.groups()
        if (self.time / 60) % self.split_time == 0:
            print("duplicate!")
            self.groups()[0].add(Virus(self.rect.center,self.split_time)) #add a new virus













def main():
    # Game loop
    global running
    virus1 = Virus((300,300),5)
    viruses.add(virus1)
    while running:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((26, 255, 255))

        text = font.render(f"Virus Count: {len(viruses)}", True, (255, 0, 0))
        text_rect = text.get_rect()

        # SCENARIO 1: Viruses overwhelm the doctors
            # 2) updates the text to say 'you
            # are overwhelmed'
             # 'end the round'
        # SCENARIO 2: Doctors eliminate all viruses
            # updates the text to say 'Outbreak contained'
        # END THE ROUND: 
            # 1) sprites stop updating
            # 2) after a few seconds, move onto the next
            # round (HINT: call init again, Group.empty())
            # --> clear the sprites from both groups
            # --> change the text back to bacteria count
            # --> draw new sprites

        # If the round isn't over,
        # testVirus.update()
        screen.blit(text, text_rect)
        screen.blit(virus1.image, virus1.rect)
        viruses.update()
        viruses.draw(screen)


        pygame.display.flip()


if __name__ == "__main__":
    main()