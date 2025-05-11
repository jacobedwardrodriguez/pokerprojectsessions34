
"""
This module defines a PokerHand class that draws a 5-card hand from a deck and
analyzes it for various poker hand types. Also includes a simulation to estimate
the probability of drawing a full house.
"""

from deck import Deck, Card

class PokerHand:
    def __init__(self, deck):
        """
            Draw 5 cards from the deck to create the hand.

            Args:
                deck (Deck): A deck from which to deal cards.
            """
        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        return self._cards
    """List[Card]: The list of 5 cards in the hand."""

    def __str__(self):
        return str(self.cards)
    """Return a string representation of the hand."""

    @property
    def is_flush(self):
        for card in self.cards[1:]:
            if self.cards[0]. suit != card.suit:
                return False
            return True
    """Check if all cards have the same suit."""

    @property
    def is_full_house(self):
        return self.number_matches == 8
    """Check if the hand is a full house (3 of a kind + a pair)."""

    @property
    def number_matches(self):
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    """
          Total number of pairwise rank matches. Used for internal classification logic.
          """

    @property
    def is_pair(self):
        if self.number_matches == 2: # simple
            return True
        return False
    """Check if the hand has exactly one pair."""

    @property
    def is_two_pair(self):
        return self.number_matches == 4 # more advanced
    """Check if the hand has two separate pairs."""

    @property
    def is_trips(self):
        if self.number_matches == 6:
            return True
        return False
    """Check if the hand has three of a kind."""

    @property
    def is_quads(self):
        if self.number_matches == 12:
            return True
        return False
    """Check if the hand has four of a kind."""

    @property
    def is_straight(self):
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4
    """
        Check if the hand is a straight (5 cards in sequence).

        Returns:
            bool: True if the hand is a straight and not a full house/pair/etc.
        """

count = 0
matches = 0
while matches < 10:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)

    if hand.is_full_house:
        matches += 1
        # print(hand)
    count += 1

print(f"Probability of a full house is {100*matches/count}%")


