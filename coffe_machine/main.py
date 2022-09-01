from coffee_machine_data import menu as menu
from coffee_machine_data import resources as resources

machine_on = True

while machine_on == True:
    user_wish = input("What would you like? (espresso/latte/cappuccino): ")
    while user_wish != "espresso" and user_wish != "latte" and user_wish != "cappuccino" and user_wish != "off" and user_wish != "report":
        user_wish = input("Please give a valid answer.\nWhat would you like? (espresso/latte/cappuccino): ")

    if user_wish == "off":
        print("Bye!")
        machine_on = False

    if user_wish == "report":
        for resource in resources:
            print(resource.capitalize(), ": ", resources[resource])


    if user_wish != "report" and user_wish != "off":
        water = menu[user_wish]["ingredients"]["water"]
        milk = menu[user_wish]["ingredients"]["milk"]
        coffee = menu[user_wish]["ingredients"]["coffee"]
        print(water, milk, coffee)
        if water > resources["water"]:
            print("Sorry, not enough water.")
            enough_resources = False
        elif milk > resources["milk"]:
            print("Sorry, not enough milk.")
            enough_resources = False
        elif coffee > resources["coffee"]:
            print("Sorry, not enough coffee.")
            enough_resources = False
        else:
            enough_resources = True
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee


    if user_wish != "report" and user_wish != "off":
        price = menu[user_wish]["cost"]
        if enough_resources == True:
            print(f"Enough resources available. It will cost you {price}$. Please insert money: ")
            quarters = int(input("Quarters: "))
            dimes = int(input("Dimes: "))
            nickles = int(input("Nickles: "))
            pennies = int(input("Pennies: "))
            user_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            print(f"You paid {user_money}$.")
            while price > user_money:
                print(
                    f"You don't have enough money. You still need {round(price - user_money, 2)}$. Please give more money: ")
                quarters = int(input("Quarters: "))
                dimes = int(input("Dimes: "))
                nickles = int(input("Nickles: "))
                pennies = int(input("Pennies: "))
                user_money = user_money + quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if price == user_money:
                print("Thank you. Preparing... ")
            else:
                print(f"Here is your rest of {round(user_money - price, 2)}$. Preparing... ")
            print("Here is your coffee: ☕ \n\n")
