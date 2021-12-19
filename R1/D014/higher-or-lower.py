# Library
from art import logo, vs
from game_data import data
import os
import random


# Defined functions

# Clear the console
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


# Compare two chosen person
def check_answer(personA, personB, answer):
    if (personA['follower_count'] > personB['follower_count'] and answer == 'a') or (personA['follower_count'] < personB['follower_count'] and answer == 'b'):
        return True
    else:
        return False


game_on = True
score = 0
print(logo)

while game_on:
    chosen_A = random.choice(data)
    print(f"Compare A: {chosen_A['name']}, {chosen_A['description']}, {chosen_A['country']}")
    print(vs)
    chosen_B = random.choice(data)
    print(f"Compare B: {chosen_B['name']}, {chosen_B['description']}, {chosen_B['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    clearConsole()
    print(logo)
    if check_answer(chosen_A, chosen_B, answer):
        score += 1
        print(f"You're ringt! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_on = False