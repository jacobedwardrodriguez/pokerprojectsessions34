"""
This module defines a  Card and Deck system for standard playing cards.
Cards support comparison based on rank, and the Deck supports shuffling and dealing.
"""
import random

class Card:
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♠", "♥", "♦" ]
    def __init__(self, suit, rank):
        if rank not in self.RANKS:
            raise ValueError("Invalid rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid suit")
        """
             Initialize a Card object.

             Args:
                 suit (str): Suit of the card (♣, ♠, ♥, ♦).
                 rank (str): Rank of the card ("2" to "A").

             Raises:
                 ValueError: If the suit or rank is invalid.
             """
        self._suit = suit
        self._rank = rank

    def __eq__(self, other):
        return self.rank == other.rank

    """
         Check if two cards have the same rank.
         Args:
             other (Card): Another card to compare.
         Returns:
             bool: True if ranks are equal.
         """
    def __gt__(self, other):
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)
    """
        Compare two cards by rank.
        Args:
            other (Card): Another card to compare.
        Returns:
            bool: True if this card has a higher rank than the other.
        """
    def __str__(self):
        return f"{self._rank}{self._suit}"
    """
          Return a string representation of the card.
          Returns:
              str: Card in the format 'RankSuit', e.g., 'Q♠'.
          """
    def __repr__(self):
        return self.__str__()
    """Return official string representation."""

    @property
    def suit(self):
        return self._suit
    """str: The suit of the card."""

    @property
    def rank(self):
        return self._rank
    """str: The rank of the card."""

class Deck:
    def __init__(self):
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit, rank))

    def __str__(self):
        return str(self._deck)
    """
        Return string representation of the deck.
        Returns:
            str: List of cards as a string.
        """
    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop()

    """
         Deal one card from the top of the deck.
         Returns:
             Card: The top card of the deck.
         Raises:
             IndexError: If the deck is empty.
         """

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())





