from card import Card
import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        for index in range(len(self.cards) - 1):
            num = random.randint(index + 1, len(self.cards) - 1)
            temp = self.cards[index]
            print("Index: {} Num: {}".format(index, num))
            self.cards[index] = self.cards[num]
            self.cards[num] = temp
            
    def print_deck(self):
        for card in self.cards:
            card.print_card()
    
    def deal_card(self, player):
        if len(self.cards) > 0:
            card = random.choice(self.cards)
            player.hand.append(card)
            self.cards.remove(card)
        else:
            print("No cards left!")
