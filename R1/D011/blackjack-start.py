import random
from art import logo

def sum_card(cards):
    sum = 0
    for card in cards:
        sum += card
    return(sum)

def deal_card(p_cards, c_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    p_cards.append(random.choice(cards))
    if sum_card(p_cards) > 21:
        p_cards[-1] = 1
    c_cards.append(random.choice(cards))

def play_game():
    print(logo)
    player_cards = []
    computer_cards = []
    deal_card(player_cards, computer_cards)
    deal_card(player_cards, computer_cards)
    should_go = True
    while should_go and sum_card(player_cards) <= 21:
        print(f"Your cards: {player_cards}, current score: {sum_card(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            deal_card(player_cards, computer_cards)
        else:
            should_go = False
        
    else:
        print(f"Your final hand: {player_cards}, final score: {sum_card(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum_card(computer_cards)}")
        if sum_card(player_cards) > 21:
            print("You went over. You lose")
        elif sum_card(player_cards) > sum_card(computer_cards):
            print("You win")
        elif sum_card(player_cards) == sum_card(computer_cards):
            print("Draw")
        else:
            print("You lose")

print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()