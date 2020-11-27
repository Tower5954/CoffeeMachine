MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
bank = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def sufficient_resources(order_ingredients):
    """Returns True if order can be made and False if insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} for your order")
            return False
    return True


def process_coins():
    """"Returns how many coins have been inserted"""
    total = 0
    print("Please insert coins")
    total += int(input("How many Pounds coins?: ")) * 1.00
    total += int(input("How many 50p coins?: ")) * 0.50
    total += int(input("How many 20p coins?: ")) * 0.20
    total += int(input("How many 10p coins?: ")) * 0.10
    total += int(input("How many 5p coins?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """Return True if the payment is accepted or False if insufficient funds"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Thank you and here is £{change}p as your change")
        global bank
        bank += drink_cost
        return True
    else:
        print("Sorry that is not enough. Money refunded")
        return False


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:£{bank}")
    else:
        drink = MENU[choice]
        if sufficient_resources(drink["ingredients"]):
            payment = process_coins()
            transaction_successful(payment, drink["cost"])

# TODO 1 Prompt user by "what would you like? (espresso/latte/cappuccino)
# TODO 2 turn off the coffee machine by entering "off" to the prompt
# TODO 3 Print report
# TODO 4 Check resources sufficient
# TODO 5 Process coins
# TODO 6 Check transaction successful
# TODO 7 Make coffee
