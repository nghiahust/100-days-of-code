rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
choices = [rock,paper,scissors]
your_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
if your_number > 2 or your_number < 0:
    print("You type invalid number, you lose!")
else:
    your_choice = choices[your_number]
    print(f"Your chose: {your_choice}")
    com_choice = random.choice(choices)
    print(f"Computer chose:{com_choice}")
    if com_choice == choices[your_number - 1]:
        print("You win")
    elif com_choice == choices[your_number]:
        print("Draw")
    else:
        print("You lose")