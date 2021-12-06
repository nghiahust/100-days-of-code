print("Welcome to treasure island")
print("Your mission is to find the treasure")

# Step one
choose1 = input("Do you wan to go left or right?\n")
if choose1.lower() != "left":
    print("Fall in a hole. Game Over.")
else:
    # Step two
    choose2 = input("Do you want to swim or wait?\n")
    if choose2.lower() != "wait":
        print("Attacked by trout. Game Over.")
    else:
        # Step three
        choose3 = input("Which door?\n")
        if choose3.lower() == "red":
            print("Burn in fire. Game Over.")
        elif choose3.lower() == "blue":
            print("Eaten by beasts. Game Over.")
        elif choose3.lower() == "yellow":
            print("You Win!")
        else:
            print("Game Over.")