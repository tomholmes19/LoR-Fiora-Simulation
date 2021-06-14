import random

from . import generics

class Entreat(generics.Spell):
    def __init__(self, name="Entreat", cost=2, speed="Burst") -> None:
        super().__init__(name, cost, speed)
    
    def play(self, hand, deck) -> None:
        """
        Draw a champion from the Deck

        Input:
            hand (Hand): hand to draw to
            deck (Deck): deck to draw from

        Return:
            None
        """
        champions = [card for card in deck.cards if isinstance(card, generics.Champion)]
        champion = random.choice(champions)
        hand.draw(deck=deck, card=champion)
        return None