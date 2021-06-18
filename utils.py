import cards
import card_containers

def check_fiora(hand) -> bool:
    """
    Checks if a Fiora or Entreat card is in Hand

    Input:
        hand (Hand): the hand to check
    
    Return:
        in_hand (bool): True if Fiora in hand, False otherwise
    """
    in_hand = False
    for card in card_containers.hand:
        if isinstance(card, cards.fiora.Fiora) or isinstance(card, cards.entreat.Entreat):
            in_hand = True
            break
    
    return in_hand

def deck_builder(card_dict, shuffle=True):
    """
    Builds a deck from a dictionary of cards in the format 
        <Card>: number of this card
    
    Input:
        card_dict (dict): dictionary of cards
        shuffle (bool): if True, shuffle deck before returning
    
    Return:
        deck (Deck): Deck object containing the cards from card_dict
    """
    cards = []

    for card, n in card_dict.items():
        cards += [card for _ in range(n)]
    
    deck = card_containers.Deck(cards=cards)

    if shuffle:
        deck.shuffle()

    return deck

if __name__ == "__main__":
    cards = {
        cards.generics.Card(name="_", cost=0): 34,
        cards.fiora.Fiora(): 3,
        cards.entreat.Entreat(): 3
    }

    deck = deck_builder(cards)
    print(deck)