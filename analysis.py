import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sim import simulation
import cards

cards_to_draw = {
    cards.fiora.Fiora(): 3,
    cards.entreat.Entreat(): 3
}
n = 100
draws = pd.Series([simulation(cards_to_draw) for _ in range(n)])

#TODO: fix this
counts = draws.value_counts()
sns.barplot(sorted(counts.index), y=counts.sort_index().values, data=counts)
plt.show()