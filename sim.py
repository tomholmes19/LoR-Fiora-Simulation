from cards.generics import *
from cards.fiora import Fiora
from cards.entreat import Entreat
from card_containers import *
import utils

def simulation():
    cards = {
        Card(name="_", cost=0): 34,
        Fiora(): 3,
        Entreat(): 3
    }