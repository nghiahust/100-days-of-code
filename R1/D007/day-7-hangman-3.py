import random

# List of word
word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
for _ in range(0, word_length):
    display += "_"

# Game play
count = word_length
while count > 0:
    your_guess = input("Guess a letter: ").lower()
    for i in range(0, word_length):
        if your_guess == chosen_word[i]:
            display[i] = chosen_word[i]
            count -= 1
    print(display)
