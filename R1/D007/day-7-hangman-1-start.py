import random

# List of word
word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word
chosen_word = random.choice(word_list)

# Game play
your_guess = input("Guess a letter: ").lower()
for char in chosen_word:
  if char == your_guess:
    print("Right")
  else:
    print("Wrong")