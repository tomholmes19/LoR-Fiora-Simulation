import cards
import card_containers

def in_hand(hand, *args) -> bool:
    """
    Checks if a card with name specified in *args is in hand

    Input:
        hand (Hand): the hand to check
        *args (tuple): tuple of card names to check
    
    Return:
        in_hand (bool): True if card type in hand, false otherwise
    """

    in_hand = False
    for card in hand:
        if card.name in args:
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
    card_list = []

    for card, n in card_dict.items():
        card_list += [card for _ in range(n)]
    
    deck = card_containers.Deck(cards=card_list)

    if shuffle:
        deck.shuffle()

    return deck

if __name__ == "__main__":
    card_dict = {
        cards.generics.Card(name="_", cost=0): 34,
        cards.fiora.Fiora(): 3,
        cards.entreat.Entreat(): 3
    }

    deck = deck_builder(card_dict)
    print(deck)

def sim_draw(current_draw, hand, deck) -> int:
    draw = current_draw + 1
    hand.draw(deck)
    return draw