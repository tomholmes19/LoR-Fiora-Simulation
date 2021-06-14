from cards.generics import *
from cards.fiora import Fiora
from cards.entreat import Entreat
from card_containers import *


fiora = Fiora()
fiora.speak()
print(fiora)

entreat = Entreat()
print(entreat)

print("=====")

cards = [Card(name="a", cost=0) for _ in range(8)] + [Fiora(), Entreat()]
deck = Deck(cards)
print(deck)

hand = Hand()
hand.draw(deck)
print(hand)

hand.play(card=hand.cards[0], hand=hand, deck=deck)
print(hand)
print(deck)