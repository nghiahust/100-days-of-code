from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
my_maker = CoffeeMaker()
my_money = MoneyMachine()
my_menu = Menu()


while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        my_maker.report()
        my_money.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_maker.is_resource_sufficient(drink):
            if my_money.make_payment(drink.cost):
                my_maker.make_coffee(drink)
