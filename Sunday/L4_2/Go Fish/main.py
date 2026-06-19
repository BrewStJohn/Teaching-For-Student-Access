import random
# 1) Create a class called "Card"
# Properties: suit, rank
# Methods: print_card - this should print out to the console
# what the card is. i.e. 5 of Spades
# CHALLENGE 1: When creating a class, put it into its own
# seperate module. Have a 'main.py' to run your game
# and these classes.
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def print_card(self):
        # Aiden: prints the rank and suite of the card (self)
        print(f"{self.rank} of {self.suit}")
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

testCard = Card('Clubs', 9)
print(testCard)
# CHALLENGE 2: Create a __repr__ method for the Card class
# and use that instead of print_card.

# 2) Create a class called "Deck"
class Deck:
    def __init__(self):
        # Properties: a list called 'cards' that contains
        # 52 instances of the Card class 
        # --> for each suite (heart, spades, diamonds, clubs),
        # --> create a card with rank 1 (Ace) to 14 (King)
        self.cards = []

        # we could do this, but its not very efficient..
        # self.cards.append(Card("Heart", 13))
        # self.cards.append(Card("Heart", 12))
        # self.cards.append(Card("Heart", 11))

        # we are gonna need a for loop
        suites = ["Hearts", "Diamonds", "Spades", "Clubs"]
        # Edwards Solution
        # ranks = ['Ace', '1', '2', '3'] #..
        for suite in suites:
            for i in range(1, 14):
                # Aadya: Adding cards to the deck
                self.cards.append(Card(suite, i))

    # Methods:
    # 1) print_deck - this should print out to the console
    # all of the cards in the deck in the same format 
    # as print_card.
    # If you would perfer using a magic method, go ahead
                
    def print_deck(self):
        for card in self.cards:
            # using the print_card() method to 
            # print out all the cards in the deck
            card.print_card()

    # 2) CHALLENGE 2: shuffle 
    # Loop through all the cards until the second to last in
    #  the deck.
    # ■ On each iteration pick a random card from 
    # within the interval: current card+1 through the 
    # end of the deck.
    # ■ Swap the current card and the randomly selected card
    # REMEMBER TO USE A TEMP VAR!

    def shuffle(self):
        for index in range(len(self.cards) - 1):
            num = random.randint(index + 1, len(self.cards) - 1)
            temp = self.cards[index]
            print("Index: {} Num: {}".format(index, num))
            self.cards[index] = self.cards[num]
            self.cards[num] = temp

    def deal_card(self, player):
        if len(self.cards) > 0:
            # takes a card from the deck and puts 
            # it into the players hand
            player.hand.append(self.cards.pop())
        else:
            print("No cards left!")

newDeck = Deck()
newDeck.print_deck()

# What should a Player class contain?
# PROPERTIES: Score, Hand (a list of Cards), Name
# METHODS: print_hand
# check_hand(when given a rank, check to see if the player has it.
# give all the player that asked all the cards they have with that rank)
# HINT: return

class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.score = 0

    def print_hand(self):
        # iterate through all the values of the hand
        for card in self.hand:
            # print out those values
            card.print_card()
    
    # check_hand --> when given a rank, check to see if the player 
    # has it. Return all the cards with that rank. If they dont
    # have any of that rank, return "".
    # HINT: return


player1 = Player("Dylan")
player1.hand.append(Card("Hearts", 10))
player1.print_hand()

# AFTER THIS: You're making the game!
# how does the game work? Look at the chat.
# 1) Create players + deck
# --> shuffle the deck
# 2) Give all the players a hand
# 3) turns?
# --> when its a player turn, you can see their hand
# --> the player asks for a rank they want to fish for
# --> then specifies a player to fish from
# --> ... and so on































