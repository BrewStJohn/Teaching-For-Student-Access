from card import Card;
import random
# TASK: Create a class called "Deck" that:
# a) has one property called 'cards' that is a list of 52 cards.
# --> You need to generate each of these cards.
# HINT: append, module

# TEST: Creating an instance of Deck in main, and then picking 
# a random card from the deck to draw to the screen

# deck = new Deck();
# testCard = deck.cards[random.randint(0, 51)]
# draw the test card to the screen.

class Deck():
    def __init__(self):
        # DECK PROPERTIES:
        # 1) A list to store cards
        # how do we make the 52 cards in the deck?
        suites = ["Hearts", "Spades", "Diamond", "Clubs"]
        self.cards = []
        for suite in suites:
            for i in range(1, 14):
                self.cards.append(Card(i, suite))

    # DECK METHODS:
    # 1) Shuffle:
    # --> How do I do that?
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            idx = random.randint(0, i-1)
            temp = self.cards[idx]
            self.cards[idx] = self.cards[i]
            self.cards[i] = temp
            # a) we need to use a tmp variable 
            # to keep track of what we're swapping
            # b) starting at the top of the list, pick a random card,
            # swap the top of the list and that card, and then move down the list 1 
            # till you get to the end of the list

    # 2) Dealing cards?
    def deal(self):
        # if our list is not empty,
        if (len(self.cards) > 0):
            # --> Pop the top card off the list
            return self.cards.pop()
            # if it is, we need to add all the cards back




