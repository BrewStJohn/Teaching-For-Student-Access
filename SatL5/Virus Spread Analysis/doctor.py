import pygame
import random

class Doctor(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("doctor.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        # SOLUTION 1: 
        # self.speed = pygame.math.Vector2(random.randint(-5,5),random.randint(-5,5)) # --> Vector2(0,0)
        # SOLUTION 2:
        self.speed = pygame.math.Vector2(2)
        self.speed.rotate_ip(random.randint(0,360))

    def update(self):
        self.rect = self.rect.move(self.speed)
        # CHALLENGE: Try to get them to reflect off the walls
        if the time passed
            duplicate -- add virus where this guy is and add him to the group
            self.groups[0]