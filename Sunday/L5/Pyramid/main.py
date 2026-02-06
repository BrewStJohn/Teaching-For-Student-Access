# 1) Create a basic pygame application
# with a green background
import pygame as py
from card import Card
from deck import Deck

py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

new_deck = Deck()

# print("before shuffle")
# for i in range(len(new_deck.cards)-1):
#     print(new_deck.cards[i].rank, new_deck.cards[i].suite)

new_deck.shuffle()
# print("after shuffle")

# for i in range(len(new_deck.cards)-1):
#     print(new_deck.cards[i].rank, new_deck.cards[i].suite)

card = new_deck.deal()
card.rect.center = (200, 200)
card2 = new_deck.deal()
# new_card = Card(10, "Diamond") # this should create a card
# new_card.rect.center = (500, 500)
# card_image = py.image.load("Pyramid/PNG/Medium/Spades 1.png")

def process_events():
    global running
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

def main(): # run my game
    while running:
        process_events()

        screen.fill("green")
        # screen.blit(new_card.image, new_card.rect)
        screen.blit(card.image, card.rect)
        screen.blit(card2.image, card2.rect)
        py.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


