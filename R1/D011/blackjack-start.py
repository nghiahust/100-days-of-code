import random
from art import logo

def sum_card(cards):
    total = 0
    for card in cards:
        total += card
    return(total)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def play_game():
    player_cards = []
    computer_cards = []
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    should_go = True
    while should_go and sum_card(player_cards) <= 21:
        print(f"Your cards: {player_cards}, current score: {sum_card(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_cards.append(deal_card())
        else:
            should_go = False
    else:
        print(f"Your final hand: {player_cards}, final score: {sum_card(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum_card(computer_cards)}")
        
        pscore = sum_card(player_cards)
        cscore = sum_card(computer_cards)

        if pscore == cscore:
            print("Draw")
        elif pscore == 21:
            print("Win with a Blackjack.")
        elif cscore == 21:
            print("Lose, opponent has Blackjack.")
        elif pscore > 21:
            print("You went over. You lose")
        elif pscore > cscore:
            print("You win")
        else:
            print("You lose")

print(logo)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()