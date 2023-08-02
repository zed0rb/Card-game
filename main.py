import random

# global variables used for build deck and track value for rank
SUITS = ("♠", "♥", "♦", "♣")
RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")


class Deck:
    def __init__(self):
        self.cards = []
        self.suits = SUITS
        self.ranks = RANKS
        self.build_deck()

    # build the deck
    def build_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(suit + " " + rank)
        return self.cards

    # method to split the deck in 2
    def split_in_two(self):
        return self.cards[:26], self.cards[26:]

    # shuffle the deck
    def shuffle(self):
        return random.shuffle(self.cards)
