class Card:
    def __init__(self, Suit, Rank):
        self.suit = Suit
        self.rank = Rank
        
    def print_card(self):
        print(f"{self.rank} of {self.suit}")
