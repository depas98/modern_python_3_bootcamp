# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should display information on how many cards are in the deck (e.g.
# "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most
# that many cards from the deck (it may need to remove fewer if you request more cards than are
# currently in the deck!). If there are no cards left, this method should return a ValueError
# with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards.
# If there are cards missing from the deck, this method should return a ValueError  with the message
# "Only full decks can be shuffled".
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single
# card from the deck.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal
# method to deal a list of cards from the deck.

from random import shuffle


class Card:
    possible_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    possible_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, value, suit):
        if suit not in Card.possible_suits:
            raise ValueError(f"The suite {suit} is not valid")
        if value not in Card.possible_values:
            raise ValueError(f"The value {value} is not valid")

        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        self.cards = [Card(card_value, card_suit)
                      for card_value in Card.possible_values
                      for card_suit in Card.possible_suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def _deal(self, amount):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")

        actual = min([amount, self.count()])

        dealt_cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]

        return dealt_cards

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, amount):
        return self._deal(amount)


card1 = Card(Card.possible_values[0], Card.possible_suits[0])
print(card1)
card2 = Card("K", "Spades")
print(card2)

my_deck = Deck()
my_deck.shuffle()
print(my_deck.count())

my_hand = my_deck.deal_hand(5)
print(my_hand)
print(my_deck.count())

card = my_deck.deal_card()
print(card)
print(my_deck.count())
