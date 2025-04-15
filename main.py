from card_data_cleaning import card_df

import time

from cards import print_blank, print_card

from war_cards import blackjack_game

keep_playing = 1
rounds = 0

while keep_playing:
    if rounds == 0:
        play_blackjack = input('Would you like to play a round of blackjack? (Enter yes/y or no/n): \n')
    else:
        play_blackjack = input('Another round? (Enter yes/y or no/n): \n')

    if play_blackjack.lower() == 'yes' or play_blackjack.lower() == 'y':
        blackjack_game()
        rounds += 1
    elif play_blackjack.lower() == 'no' or play_blackjack.lower() == 'n':
        keep_playing = 0
        print(f'You played {rounds} rounds.')
        print('Thanks for playing!')
        continue
    else:
        print('Please enter a valid input of yes/y or no/n')

