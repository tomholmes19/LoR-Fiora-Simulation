import cards
import card_containers
import utils

def simulation():
    # Step 1: Initialize variables
    card_dict = {
        cards.generics.Card(name="_", cost=0): 34,
        cards.fiora.Fiora(): 3,
        cards.entreat.Entreat(): 3
    }

    deck = utils.deck_builder(card_dict)
    hand = card_containers.Hand()

    current_draw = 0

    # Step 2: Simulate game
    while not utils.in_hand(hand, "Fiora", "Entreat"):
        # Mulligan round
        if current_draw in [0, 4]:
            # If current_draw==4, i.e. drawn 4 generics, replace all cards in hand
            if current_draw == 4:
                hand.replace_all(deck)

            # Draw 4 cards
            for _ in range(4):
                current_draw = utils.sim_draw(current_draw, hand, deck)

                # break loop if previously drawn card is Fiora or Entreat
                if hand[-1].name in ["Fiora", "Entreat"]:
                    break
        
        # Standard round
        else:
            current_draw = utils.sim_draw(current_draw, hand, deck)

    return current_draw

print(simulation())