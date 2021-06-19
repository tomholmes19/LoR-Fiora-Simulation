import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from sim import simulation
import cards

sns.set_theme()

def sim_wrapper(n, num_fiora=3, num_entreat=3, deck_size=40, mulligan_size=4):
    cards_to_draw = {
        cards.fiora.Fiora(): num_fiora,
        cards.entreat.Entreat(): num_entreat
    }

    draws = [simulation(cards_to_draw, deck_size, mulligan_size) for _ in range(n)]

    m = max(draws)
    counts = [0]*m
    for x in draws:
        counts[x-1] += 1

    probs = np.array(counts)/n

    sns.barplot(
        x=np.array(range(1,m+1)),
        y=probs
    )

    print("Prob less_eq 11:\t", sum(probs[:11]))
    print(np.mean(draws))
    plt.show()

sim_wrapper(1000)