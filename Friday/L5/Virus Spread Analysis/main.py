import pygame

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
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load('Virus Spread Analysis\\virus.png')
        self.image = pygame.transform.smoothscale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update():
        pass
        # how do I get this guy to move around?
        # how can we get viruses to duplicate?

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