import random

people = input('Who have lunch today, seperate with ", ": ')
list_people = people.split(", ")
seed = len(list_people)

print(f"{list_people[random.randint(0, seed - 1)]} is going to buy the meal today!")

# choosen_one = random.choice(list_people)