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

resources = {
    "water(milliliters)": 300,
    "milk(milliliters)": 200,
    "coffee(grams)": 100,
}

def check_water(flavour):
    if resources["water(milliliters)"] >= MENU[flavour]["ingredients"]["water"]:
        return 1
    return 0

def check_milk(flavour):
    if resources["milk(milliliters)"] >= MENU[flavour]["ingredients"]["milk"]:
        return 1
    return 0

def check_coffee(flavour):
    if resources["coffee(grams)"] >= MENU[flavour]["ingredients"]["coffee"]:
        return 1
    return 0

def process_payment(flavour):
    print("Please insert coin/s")
    penny = float(input("penny/ies: "))
    nickel = float(input("nickel/s: "))
    dime = float(input("dime/s: "))
    quarter = float(input("quarter/s: "))
    total = (penny * 0.01) + (nickel * 0.05) + (dime * 0.1) + (quarter * 0.25)
    if total < MENU[flavour]["cost"]:
        print("You are low on money")
        return 0
    else:
        change = total - MENU[flavour]["cost"]
        print(f"Here's your change: {change}$")

        return 1

def subtract_resources(flavour):
    if flavour == "espresso":
        resources["water(milliliters)"] -= MENU[flavour]["ingredients"]["water"]
        resources["coffee(grams)"] -= MENU[flavour]["ingredients"]["coffee"]
    else:
        resources["water(milliliters)"] -= MENU[flavour]["ingredients"]["water"]
        resources["coffee(grams)"] -= MENU[flavour]["ingredients"]["coffee"]
        resources["milk(milliliters)"] -= MENU[flavour]["ingredients"]["milk"]

not_done = True

while not_done:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "end":
        not_done = False
    else:
        if choice.lower() == "report":
            for key in resources:
                print(key + ": " + str(resources[key]))
        if choice in MENU:
            ingredients = MENU[choice]["ingredients"]
            # Check ingredients
            if "water" in ingredients and resources["water(milliliters)"] < ingredients["water"]:
                print("You are short on water")
            elif "milk" in ingredients and resources["milk(milliliters)"] < ingredients["milk"]:
                print("You are short on milk")
            elif "coffee" in ingredients and resources["coffee(grams)"] < ingredients["coffee"]:
                print("You are short on coffee")
            else:
                if process_payment(choice):
                    subtract_resources(choice)
                    print(f"Here's your {choice}! Enjoy!")
        else:
            print("Invalid input. Please choose from espresso, latte, or cappuccino.")







