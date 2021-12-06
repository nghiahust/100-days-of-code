print("Welcome to Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() + name2.lower()

# Count TRUE
count_true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
count_love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

score = count_true * 10 + count_love

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")