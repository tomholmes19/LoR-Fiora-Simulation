from cards import entreat
import cards
import card_containers
import utils

def simulation(cards_to_draw, deck_size=40, mulligan_size=4):
    """
    Runs a single simulation to find the number of draws needed to draw a card type in cards_to_draw,
    a dictionary of the format
        <Card>: number of this card

    Input:
        cards_to_draw (dict): dictionary of cards to draw for in the simulation
    
    Return:
        current_draw (int): the draw on which a card in cards_to_draw is drawn
    """
    # Initialize variables

    card_names = [card.name for card in cards_to_draw]

    non_generics = sum([num for num in cards_to_draw.values()])
    generics = deck_size - non_generics

    card_dict = {cards.generics.Card(name="_", cost=0): generics} | cards_to_draw
    deck = utils.deck_builder(card_dict)

    hand = card_containers.Hand(cards=[])

    current_draw = 0

    # Simulate game
    while not utils.in_hand(hand, card_names):
        # Mulligan
        if current_draw == 2*mulligan_size:
            print(hand)
            for _ in range(mulligan_size):
                # index=0 ensures the 4 first cards added into hand are replaced
                hand.replace(deck, index=0, shuffle=False)
                deck.shuffle()

        current_draw += 1
        hand.draw(deck)

    return current_draw
