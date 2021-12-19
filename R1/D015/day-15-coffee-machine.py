# Variables
is_off = False

resources = {
    'water': {
        'quantity': 100,
        'unit': 'ml'
    },
    'milk': {
        'quantity': 50,
        'unit': 'ml'
    },
    'coffee':
    {
        'quantity': 76,
        'unit': 'g'
    }
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}


# Functions
def turn_off():
    global is_off
    is_off = True


def make_coffee(coffee_type):
    if check_resources(coffee_type):
        global resources
        process_coins(coffee_type)
        for resource in resources:
            resources[resource]['quantity'] -= MENU[coffee_type]['ingredients'][resource]


def check_resources(coffee_type):
    global resources
    for resource in resources:
        if resources[resource]['quantity'] < MENU[coffee_type]['ingredients'][resource]:
            print(f"Sorry there is not enough {resource}")
            return False
    else:
        return True


def process_coins(coffee_type):
    global MENU
    print("Please insert coins. ")
    total_coins = 0
    for coin in coins:
        added_coin = int(input(f"How many {coin}? :"))
        total_coins += coins[coin] * added_coin
    if MENU[coffee_type]['cost'] > total_coins:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        charge = round(total_coins - MENU[coffee_type]['cost'])
        print(f"Here is ${charge} in charge")
        print(f"Here is your {coffee_type}. Enjoy!")


def report():
    for resource in resources:
        print(f"{resource}: {resources[resource]['quantity']} {resources[resource]['unit']}")


# Main
while not is_off:
    command = input("What would you like? (espresso/latte/cappuccinno): ").lower()
    if command == 'off':
        turn_off()
    elif command == 'report':
        report()
    elif command in MENU:
        make_coffee(command)
    else:
        print("Command not found!")