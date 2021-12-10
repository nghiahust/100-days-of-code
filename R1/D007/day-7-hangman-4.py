# Import modules
import random
from hangman_art import logo, stages
from hangman_words import word_list

# Print out logo
print(logo)

# Randomly choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
for _ in range(0, word_length):
    display += "_"

# Game play
end_of_game = False
lives = 6
while not end_of_game:
    letter = input("Guess a letter: ").lower()
    if letter in display:
        print(f"You already guessed letter {letter}")
    for i in range(word_length):
        if chosen_word[i] == letter:
            display[i] = chosen_word[i]
    if letter not in chosen_word:
        lives -= 1
        print(f"You guessed letter {letter}, that is not correct. You lose a live.")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win")