"""
BlackJack! From Introduction to Python 
By Chris Lilley
September 19th, 2023
"""

import random


cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def deal_cards():

    return random.choice(cards)

# Calculates total of cards
def calc_total(hand):
    total = 0
    aces = 0

    for card in hand:
        if card == 'A':
            aces += 1
        else:
            total += min(cards.index(card) + 2, 10)
    for numb in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1

    return total


def main():
    # adds cool card suits around title and then centers for console
    blackjack = "\u2666\u2660Welcome to Blackjack\u2663\u2665"
    x = blackjack.center(66)
    print(x, "\n------------------------------------------------------------------")
    while True:
        print("------------------------------------------------------------------")
        new_game = input("Do you wish start a new game? (y/n): ")
        if new_game.lower() == 'y':
            # User's hand
            user_hand = [deal_cards(), deal_cards()]
            user_total = calc_total(user_hand)
            print(f'You are dealt {user_hand[0]} and a {user_hand[1]} . Your total is {user_total}.')

            # Dealer's hand
            dealer_hand = [deal_cards(), deal_cards()]
            dealer_total = calc_total(dealer_hand)
            print(f'The dealer has been dealt a {dealer_hand[0]} and a hidden card.')

            while True:
                if user_total == 21:
                    hit_stand = 's'
                else:
                    hit_stand = input("Hit or Stand(h/s):")

                if hit_stand.lower() == 'h' or hit_stand.lower() == 's':
                    if hit_stand.lower() == 'h':
                        hit_deal = deal_cards()
                        user_hand.append(hit_deal)
                        user_total = calc_total(user_hand)
                        print(f'Hit!\nYou draw a {hit_deal}. Your total is {user_total}.')

                        if user_total > 21:
                            print('You bust!\nDealer wins!')
                            break

                    elif hit_stand.lower() == 's':
                        print(f"You Stand\n"
                              f"The dealer's hidden card is a {dealer_hand[1]} and has a total of {dealer_total}.")

                        while dealer_total < 17:
                            hit_dealer = deal_cards()
                            dealer_hand.append(hit_dealer)
                            dealer_total = calc_total(dealer_hand)
                            print(f'Dealer hits\nDealer draws a {hit_dealer}. Dealer total is now {dealer_total}.')

                        if dealer_total > 21:
                            print('Dealer busts!\nYou win!')
                        elif dealer_total < user_total <= 21:
                            print('You win!')
                        elif user_total > 21:
                            print('You bust!')
                        elif dealer_total == user_total:
                            print('It\'s a tie!\nDealer wins! House always wins')
                        else:
                            print('Dealer wins!')
                        break
                else:
                    print("Please enter only h for hit or s for stand")
        elif new_game.lower() == 'n':
            print("Ok, Goodbye!")
            exit()
        else:
            print("Please enter only y or n")


if __name__ == '__main__':
    main()
