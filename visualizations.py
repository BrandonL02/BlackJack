import pandas as pd

import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator

import numpy as np

def plot_outcomes(csv_name):

    df = pd.read_csv(csv_name)

    keep_going = True
    while keep_going:
        visual = input("Would you like to see win/loss/tie totals or percentages? (Enter 't' or 'p'): \n")

        # Count wins, losses, and ties
        wins = (df['round outcome'] == 'win').sum()
        losses = (df['round outcome'] == 'loss').sum()
        ties = (df['round outcome'] == 'tie').sum()
        total_games = wins + losses + ties
        labels = ['Wins', 'Losses', 'Ties']

        if visual.lower() == 'totals' or visual.lower() == 't':

            # Create a barchart for the outcomes of the game
            values = [wins, losses, ties]
            # print(f"{wins} wins, {losses} losses, {ties} ties") # Checks count for wins, losses, and ties
            plt.bar(labels, values)
            plt.title("Player Game Results")

            # Make y-axis to show integer values
            ax = plt.gca()
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))

            plt.show()
            keep_going = False

        elif visual.lower() == 'percentages' or visual.lower() == 'p':

            # Create a pie chart for the outcomes
            win_rate = wins / total_games
            loss_rate = losses / total_games
            tie_rate = ties / total_games

            rates = np.array([win_rate, loss_rate, tie_rate])
            colors = ['#66bb6a', '#ef5350', '#ffee58']  # green, red, yellow

            plt.figure(figsize=(6, 6))
            plt.pie(rates, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
            plt.title('Blackjack Outcome Distribution')
            plt.axis('equal')  # Equal aspect ratio ensures it's a circle
            plt.tight_layout()
            plt.show()
            keep_going = False

plot_outcomes('blackjack_data.csv')

