import random

# List of word
word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word
chosen_word = random.choice(word_list)
your_result = []

# Game play
your_guess = input("Guess a letter: ").lower()

for char in chosen_word:
    if your_guess == char:
        your_result.append(char)
    else:
        your_result.append("_")
print(your_result)