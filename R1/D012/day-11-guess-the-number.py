import random

print("Welcome to the Number Guessing Game!")
print("I'm thhinking of a number between 1 and 100.")
dificulty = input("Choose a difficult. Type 'easy' or 'hard': ")
lvl_attempts = {
    'easy': 10,
    'hard': 5
    }
lives = lvl_attempts[dificulty]
chosen_num = random.choice(range(1,101))
game_on = True
while game_on and lives > 0:
    print(f"You have {lives} attemps remaining ")
    guess = int(input("Make a guess: "))
    if lives == 0:
        print("Youve've run out of guesses, you lose.")
    elif guess > chosen_num:
        print("To high.\nGuess again.")
    elif guess < chosen_num:
        print("Too low.\nGuess again.")
    else:
        print(f"You got it! The answer was {chosen_num}")
        game_on = False
    lives -= 1