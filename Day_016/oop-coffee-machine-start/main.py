import coffee_maker
import menu
import money_machine
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_coffee_maker =CoffeeMaker()
my_menu=Menu()
my_money_machine=MoneyMachine()
is_on=True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/):")

    options=my_menu.get_items()
    if choice =="report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif choice == "off":
        is_on=False
    else:
        drink = my_menu.find_drink(choice)
        if drink:
            if my_coffee_maker.is_resource_sufficient(drink):
                if my_money_machine.make_payment(drink.cost):
                    my_coffee_maker.make_coffee(drink)

