from card import Card
import random

class Deck():
    # CONSTRUCTOR:
    def __init__(self):
        ranks = 14
        suites = ['Diamond', 'Spades', 'Hearts', 'Clubs']
        # A deck should have 1 property called:
        # 'cards' that stores all 52 cards of the deck.
        self.cards = []
        # these should be Card objects.
        # for every rank
        for i in range(1, ranks):
            # for every suite
            for suite in suites:
                # add a card to the deck --> how does that work?
                # maybe make a property that is a list, and we
                newCard = Card(i, suite)
                # put new cards into that list
                self.cards.append(newCard)

    def deal(self):
        if (len(self.cards) > 0):
            return self.cards.pop()
        
    def shuffle(self):
        for i in range(len(self.cards)-1):
            swap = random.randint(i, len(self.cards)-1)
            temp = self.cards[i]
            self.cards[i] = self.cards[swap]
            self.cards[swap] = temp

# TO TEST: Pick out a random card from a deck you made
# and draw it to the screen

# OTHER THINGS THAT NEED TO BE IMPLEMENTED:
# 1) Draw/Deal method
# 2) Shuffle method