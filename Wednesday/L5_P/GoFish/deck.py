# CREATING A DECK:
# 1) A deck consists of 52 cards. One for
# each suite and each rank.
# 2) Method to print out each card in the deck
# 3) Shuffle our deck? How?
# 4) Deal a card from the deck.

from card import Card
import random
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
player1_cards = None

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    # what are some other things a deck should be able to do?
    # 1) Print out deck
    def print_deck(self):
        for card in self.cards:
            card.print_card()

    # 2) Shuffle
    def shuffle(self):
        # for each card in our deck (you can try counting forwards or backwards)
            # swap the current card and a random card in the deck. Ideally its infront of where you are counting to
            # --> dont forget to save one of the cards in a temp variable
        for index in range(len(self.cards) - 1):
            num = random.randint(index + 1, len(self.cards) - 1)
            temp = self.cards[index]
            print("Index: {} Num: {}".format(index, num))
            self.cards[index] = self.cards[num]
            self.cards[num] = temp   
    # TO TEST: Make an instance of the deck then call its shuffle method. 
    # If you print out your deck before and after, youll know.
    
    # 3) Deal
    def deal(self):
        # return card
        if len(self.cards) > 0:
            card = self.cards.pop(0)
            return card

test = Deck()
testcard = test.deal() # now equal to the first card
testcard.print_card()
testcard2 = test.deal()
testcard2.print_card()



