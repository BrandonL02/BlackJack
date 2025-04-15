from cards import print_card

import pandas as pd

def rank_to_title(rank):
    if rank == 1:
        return 'A'
    elif rank == 11:
        return 'J'
    elif rank == 12:
        return 'Q'
    elif rank == 13:
        return 'K'
    else:
        return str(rank)




#convert card csv to pandas dataframe
card_df = pd.read_csv('poker-hand-testing.csv')

#drop all except first 2 columns
card_df = card_df.drop(card_df.columns[2:], axis=1)

#drop all repeat rows
card_df = card_df.drop_duplicates()

#reset index for cleaned deck
card_df = card_df.reset_index(drop=True)


suits = ['♠', '♥', '♦', '♣']

#Assign suit string values to the deck
card_df['Suit of Card 1'] = card_df['Suit of Card 1'].apply(lambda x: suits[x - 1])

#Assign face values to cards of value = 1 or value > 10
card_df['Rank of Card 1'] = card_df['Rank of Card 1'].apply(rank_to_title)

