from resources import MENU, resources
profit = 0


def balance(type):
    is_enough = True
    for item in type:
        if type[item] >= resources[item]:
            print(f"You don't have enough {item}")
            is_enough = False
    return is_enough


def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters? "))*0.25
    total += int(input("How many dimes? "))*0.1
    total += int(input("How many nickels? "))*0.05
    total += int(input("How many pennies? "))*0.01
    return total


def transaction(money, drink_cost):
    if money>drink_cost:
        change = round(money-drink_cost, 2)
        print(f"Your change is ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("That is not enough money")
        return False


def report():
    balance_milk = resources["milk"]
    balance_water = resources["water"]
    balance_coffee = resources["coffee"]
    print(f"Water: {balance_water}ml\nMilk: {balance_milk}ml\nCoffee: {balance_coffee}g\nMoney: ${profit}")


def make_coffee(name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {name}")


is_on = True

while is_on:
    coffee_type = input("Do you want an espresso, latte, or cappuccino? ")
    if coffee_type == "off":
        is_on=False
    elif coffee_type == "report":
        report()
    else:
        drink = MENU[coffee_type]
        if balance(drink["ingredients"]):
            payment = process_coins()
            if transaction(payment, drink["cost"]):
                make_coffee(coffee_type,drink["ingredients"])





















