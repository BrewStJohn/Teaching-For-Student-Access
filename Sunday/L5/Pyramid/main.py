# 1) Create a basic pygame application
# with a green background
import pygame as py
from card import Card

py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

new_card = Card(5, "Hearts") # this should create
# a card

def process_events():
    global running
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

def main(): # run my game
    while running:
        process_events()

        screen.fill("green")
        py.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


