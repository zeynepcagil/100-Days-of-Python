resources={"water": 300,"milk":200,"coffee":100,"Money":0.0}

recipe_book={
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
def check(drink_name):
    drink_ingredients=recipe_book[drink_name]["ingredients"]
    for item in drink_ingredients:
        if drink_ingredients[item]>resources[item]:
            print(f"Sorry we don't have enough {item} .")
            return False
    return True
def calculate():
    print("Please insert coins.")
    quarter=int(input("How many quarters?"))
    dime=int(input("How many dimes?"))
    nickel=int(input("How many nickels?"))
    pennie=int(input("How many pennies?"))
    total = pennie * 0.01 + dime * 0.10 + nickel * 0.05 + quarter * 0.25
    return total

def make_coffee(drink_name):
    drink_ingredients = recipe_book[drink_name]["ingredients"]
    for item in drink_ingredients:
         resources[item]-=drink_ingredients[item]
    resources["Money"]+=recipe_book[drink_name]["cost"]
    print(f"Here is your {drink_name}. Enjoy!")


is_on=True
while is_on:
    coffee_choice=input("What would you like? (espresso/latte/cappuccino):")
    if coffee_choice == "off":
        is_on = False
        print("Turning off the coffee machine. Goodbye!")
    if coffee_choice== "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
    if coffee_choice in recipe_book:

        if check(coffee_choice):
            money_received = calculate()
            change=money_received-recipe_book[coffee_choice]["cost"]
            if change > 0:
                print(f"Here is ${change:.2f} dollars in change.")

            make_coffee(coffee_choice)
        else:
            print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry, that's not a valid choice. Please choose from espresso, latte, or cappuccino.")








