from card_data_cleaning import card_df

import time

from cards import print_blank, print_card

def calculate_hand_value(values):
    total = sum(values)
    aces = values.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def draw_cards(first_hand):
    hand = card_df.sample(n=2 if first_hand else 1)
    cards = [[hand.iloc[i, 1], hand.iloc[i, 0]] for i in range(hand.shape[0])]
    return cards

def get_card_values(cards):
    values = []
    for card in cards:
        rank = card[0]
        if rank == 'A':
            values.append(11)
        elif rank in ['K', 'Q', 'J']:
            values.append(10)
        else:
            values.append(int(rank))
    return values


def blackjack_game():
    user_cards = []
    dealer_cards = []

    def display_hand(name, cards):
        print(f"\n{name} Hand:")
        for card in cards:
            print_card(card[0], card[1])
        print(f"Total: {calculate_hand_value(get_card_values(cards))}")

    # Initial draw
    user_cards += draw_cards(True)
    dealer_cards += draw_cards(True)

    print("\nDealer's Hand:")
    print_card(dealer_cards[0][0], dealer_cards[0][1])
    print_blank()

    display_hand("Your", user_cards)

    # Check for blackjack
    user_total = calculate_hand_value(get_card_values(user_cards))
    dealer_total = calculate_hand_value(get_card_values(dealer_cards))

    if user_total == 21 and dealer_total == 21:
        print("\nPush. You both have blackjack.")
        return
    elif user_total == 21:
        print("\nYou win with blackjack!")
        return
    elif dealer_total == 21:
        display_hand("Dealer", dealer_cards)
        print("\nDealer wins with blackjack.")
        return

    # Player's turn
    while True:
        user_total = calculate_hand_value(get_card_values(user_cards))
        if user_total >= 21:
            break
        move = input("Would you like to hit or stand? (hit/h or stand/s): ").lower()
        if move in ["hit", "h"]:
            new_card = draw_cards(False)[0]
            user_cards.append(new_card)
            print_card(new_card[0], new_card[1])
            print(f"New total: {calculate_hand_value(get_card_values(user_cards))}")
        elif move in ["stand", "s"]:
            break

    user_total = calculate_hand_value(get_card_values(user_cards))
    if user_total > 21:
        display_hand("Your", user_cards)
        display_hand("Dealer", dealer_cards)
        print("\nBust! Dealer wins.")
        return

    # Dealer's turn
    display_hand("Dealer", dealer_cards)

    while calculate_hand_value(get_card_values(dealer_cards)) < 17:
        time.sleep(2)
        new_card = draw_cards(False)[0]
        dealer_cards.append(new_card)
        print_card(new_card[0], new_card[1])
        print(f"Total: {calculate_hand_value(get_card_values(dealer_cards))}")

    dealer_total = calculate_hand_value(get_card_values(dealer_cards))
    user_total = calculate_hand_value(get_card_values(user_cards))

    # Final Comparison

    if dealer_total > 21:
        print("\nDealer busted. You win!")
    elif dealer_total == user_total:
        print(f"\nPush. You both got {user_total}.")
    elif user_total > dealer_total:
        print(f"\nYou win! You got {user_total}, dealer got {dealer_total}.")
    else:
        print(f"\nDealer wins. Dealer got {dealer_total}, you got {user_total}.")
