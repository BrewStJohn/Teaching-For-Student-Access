# Create Card Class
class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def print_card(self):
        print(self.rank, self.suite)
# Create an object from the Card Class

r1 = Card("Spades", 5)

# method that prints out the card
r1.print_card()

# properties
r1.suite
r1.rank

# Can make more objects with the object constructor
# r2 = Card("Hearts", 10)
# r3 = Card("Clubs", 9)
# r4 = Card("Clubs", 11)
# r5 = Card("Spades", 6)
# r6 = Card("Diamonds", 2)
# r1.suite == "Spades"
# r3.suite == "Clubs"
