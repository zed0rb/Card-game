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

class Player:
    def __init__(self, player_deck, name):
        self.name = name
        self.deck = player_deck

    # Checks if player got cards in his deck
    def has_cards(self):
        return bool(self.deck)


class PlayerHand(Player):
    # returns player and number for cards in his deck
    def __str__(self):
        return "{} have {} cards".format(self.name, len(self.deck))

    # add cards to player deck
    def add_cards(self, add_cards):
        return self.deck.extend(add_cards)

    # remove 1 card from top of his deck
    def play_card(self):
        return self.deck.pop()

def main():

    deck = Deck()
    deck.shuffle()
    deck1, deck2 = deck.split_in_two()

    player1 = PlayerHand(deck1, "Tom")
    player2 = PlayerHand(deck2, "computer")


    # game continues till players got cards in their deck
    while player1.has_cards() and player2.has_cards():
        pot = []
        while True:
            p1_card = player1.play_card()
            p2_card = player2.play_card()
            pot.extend([p1_card, p2_card])
            print(p1_card)
            print(p2_card)

            # check who won battle or declaring war
            if RANKS.index(p1_card[2:]) > RANKS.index(p2_card[2:]):
                player1.add_cards(pot)
                print("{} won the battle".format(player1.name))
                break
            elif RANKS.index(p1_card[2:]) < RANKS.index(p2_card[2:]):
                player2.add_cards(pot)
                print("{} won the battle".format(player2.name))
                break
            else:
                pot.extend([player1.play_card(), player2.play_card()])
        print(player1)
        print(player2)
        

if __name__ == "__main__":
    main()
