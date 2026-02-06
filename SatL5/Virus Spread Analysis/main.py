# Example file showing a basic pygame "game loop"
import pygame
from doctor import Doctor

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

doctors = pygame.sprite.Group()
doctors.add(Doctor((200, 200)))
doctors.add(Doctor((300, 300)))

def process_events():
    global running
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

def run_game():
    while running:
        process_events()
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        doctors.update()
        # RENDER YOUR GAME HERE
        doctors.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    run_game()