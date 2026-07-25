class Deck:
    def __init__(self):
        self.cards = []
        # This class will have only 1
        # property called cards, a list that 
        # contains Cards.

        # 1) What is a Deck of Cards?
        # Contains multiple different types of images and..
        # --> Set of 52 Cards, with 4 different suites (Hearts, Spades, Clubs, Diamonds) 
        # --> within each suite, there are cards numbered 2 - 10, Ace, Kings, Queens, Jacks

        # SIMPLIFY:
        # Fill the self.cards list with all the Heart cards 
        # Ace of Hearts, 2 of Hearts, 3 of Hearts... Jack of Hearts, 
        # Queen of Hearts and King of Hearts
        # Add each heart card to the self.cards list
        # --> lets start simple and type each card manually
        suites = ["Hearts", "Clubs", "Spades", "Diamonds"]
        for suite in suites:
            for i in range(1,13):
                self.cards.append(Card(suite,i))


testDeck = Deck()
print(testDeck.cards)

# TASK 2:
# Create a class called Deck

# This class will have only 1
# property called cards, a list that contains Cards.

# Add a method called print_deck that prints out
# the rank and suite of the all the cards in the deck

# CHALLENGE: Create a shuffle method that randomises the 
# contents of the deck
