from card_data_cleaning import card_df

import time

from cards import print_blank, print_card


def blackjack_game():

    user_card_values = []
    dealer_card_values = []

    def draw_cards(first_hand):
        if first_hand:
            hand = card_df.sample(n=2)
            card_1 = [hand.iloc[0, 1], hand.iloc[0, 0]]
            card_2 = [hand.iloc[1, 1], hand.iloc[1, 0]]
            return card_1, card_2
        else:
            hand = card_df.sample(n=1)
            card_1 = [hand.iloc[0, 1], hand.iloc[0, 0]]
            return card_1

    def get_card_values(card):
        rank = card[0]
        if rank == 'A':
            rank = 11
        elif rank == 'J' or rank == 'Q' or rank == 'K':
            rank = 10
        return int(rank)

    # Draw and display dealer starting cards
    dealer_first_card, dealer_second_card = draw_cards(True)

    print("\nDealer's Hand")
    print_card(dealer_first_card[0], dealer_first_card[1])
    print_blank()

    # Add cards to dealer card value list
    dealer_card_values.append(get_card_values(dealer_first_card))
    dealer_card_values.append(get_card_values(dealer_second_card))

    # Draw and display user starting cards
    user_first_card, user_second_card = draw_cards(True)

    print("\nYour Hand")
    print_card(user_first_card[0], user_first_card[1])
    print_card(user_second_card[0], user_second_card[1])

    # Add cards to user card value list
    user_card_values.append(get_card_values(user_first_card))
    user_card_values.append(get_card_values(user_second_card))
    print(f"Current value : {sum(user_card_values)}")

    time.sleep(3)

    if sum(dealer_card_values) == 21 and sum(user_card_values) == 21:
        print('\nPush. You both have blackjack.')
    elif sum(user_card_values) == 21:
        print('\nYou win!')
    elif sum(dealer_card_values) == 21:
        print('\nDealer wins.')

    player_busted = 0
    user_drawn_cards = []
    dealer_drawn_cards = []

    while sum(user_card_values) < 21:
        draw_again = input('Would you like to hit or stand? (Enter hit/h or stand/s): \n')
        if draw_again.lower() == 'h' or draw_again.lower() == 'hit':
            new_card = draw_cards(False)
            user_drawn_cards.append(new_card)
            user_card_values.append(get_card_values(new_card))
            print(f"\nCurrent value : {sum(user_card_values)}")
        elif draw_again.lower() == 's' or draw_again.lower() == 'stand':
            print(f'Ending turn with {sum(user_card_values)}.')
            break
        if sum(user_card_values) == 21:
            print('BlackJack! You win!')
            break
        elif sum(user_card_values) > 21:
            player_busted = 1

    if player_busted:
        print("\nDealer's Hand")
        print_card(dealer_first_card[0], dealer_first_card[1])
        print_card(dealer_second_card[0], dealer_second_card[1])
        print(f'Final value: {sum(dealer_card_values)}')

        print("\nYour Hand")
        print_card(user_first_card[0], user_first_card[1])
        print_card(user_second_card[0], user_second_card[1])
        for x in user_drawn_cards:
            print_card(x[0], x[1])
        print(f'\nBust! Dealer wins. Final value: {sum(user_card_values)}')
    else:
        print("\nDealer's Hand")
        print_card(dealer_first_card[0], dealer_first_card[1])
        print_card(dealer_second_card[0], dealer_second_card[1])
        while sum(dealer_card_values) < 17:
            new_dealer_card = draw_cards(False)
            dealer_drawn_cards.append(new_dealer_card)
            dealer_card_values.append(get_card_values(new_dealer_card))
            print_card(new_dealer_card[0], new_dealer_card[1])
            if sum(dealer_card_values) > 21:
                print('Dealer busted. You win!')
                break
            if sum(dealer_card_values) == sum(user_card_values):
                print(f'Push. You both got {sum(dealer_card_values)}.')

            if sum(user_card_values) > sum(dealer_card_values):
                print(f'You win! You got {sum(user_card_values)} while the dealer got {sum(dealer_card_values)}')
            elif sum(dealer_card_values) < sum(dealer_card_values):
                print(f'Dealer wins. You got {sum(user_card_values)} while the dealer got {sum(dealer_card_values)}')
