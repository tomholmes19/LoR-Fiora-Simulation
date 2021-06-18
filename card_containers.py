import random

"""
Classes for objects which hold cards, i.e. the deck and hand.
"""

class CardContainer:
    def __init__(self, cards) -> None:
        self.cards = cards
    
    def __str__(self) -> str:
        card_names = [card.name for card in self.cards]
        return ", ".join(card_names)
    
    def __getitem__(self, key):
        return self.cards[key]
    
    def __len__(self):
        return len(self.cards)

class Deck(CardContainer):
    def __init__(self, cards=[]) -> None:
        super().__init__(cards)

    def shuffle(self) -> None:
        """
        Shuffles the deck

        Input:
            None
        
        Return:
            None
        """
        random.shuffle(self.cards)
        return None

class Hand(CardContainer):
    def __init__(self, cards=[]) -> None:
        super().__init__(cards)
    
    def draw(self, deck, card=None):
        """
        Draws a Card from a Deck. If card=None then draw the top most Card from the Deck.

        Input:
            deck (Deck): Deck to be drawn from
            card (Card) (optional): specific card to draw from deck
        
        Return:
            None
        """
        if card is None:
            top_card = deck.cards.pop()
            self.cards.append(top_card)
        else:
            deck.cards.remove(card)
            self.cards.append(card)

        return None
    
    def replace(self, deck, index, shuffle=True) -> None:
        """
        Puts a Card from Hand onto the top of the Deck

        Input:
            deck (Deck): Deck to receive the Card
            index (int): index of Card in Hand
            shuffle (bool): if True, shuffle the Deck after replacement
        
        Return:
            None
        """
        card = self[index]
        self.cards.remove(card)
        deck.cards.append(card)

        if shuffle:
            deck.shuffle()
        
        return None
    
    
    def play(self, index, **kwargs) -> None:
        """
        Plays a card in hand

        Input:
            index (int): index of Card in Hand

        Return:
            None
        """
        card = self[index]
        card.play(**kwargs)
        self.cards.remove(card)

        return None
