# Coffee maching Project
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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def show_resources():
    """Shows resources and returns amount of resources in an array"""
    current_resources = []
    for element in resources:
        #print(element + ": " + str(resources[element]))
        current_resources.append(int(resources[element]))
    return current_resources
def consumer_choice():
    """Prints the menu and takes choice of customer and the necessary ingredients"""
    choice = []
    print("Welcome to the Coffee Machine")
    for option in MENU:
     print(option + ":  $" + str(MENU[option]['cost']))
    consumer_selection = input("Please make a selection: ")
    if consumer_selection == 'resources':
        show_resources()
        consumer_selection = input("Please make a selection: ")
    for ingredient in MENU[consumer_selection]['ingredients']:
        choice.append(MENU[consumer_selection]['ingredients'][ingredient])
    choice.append(MENU[consumer_selection]['cost'])
    return choice
def check_ingredients(choice, available_resources):
    """Checks the consumer choice to see if there are enough ingredients and updates ingredients"""
    for item in range(3):
        if available_resources[item] >= choice[item]:
            available_resources[item] -= choice[item]
        else:
            return False
    return True
def take_money(cost):
    """Takes cost and payment, returns change"""
    quarter_amount = int(input("How many quarters inserted?"))*0.25
    dime_amount = int(input("How many dimes inserted?"))*0.1
    nickel_amount = int(input("How many nickels inserted?"))*0.05
    penny_amount = int(input("How many pennies inserted?"))*0.01
    sum = quarter_amount + dime_amount + nickel_amount + penny_amount
    if cost > sum:
        print("Not enough coins, please try again!")
        return cost
    print("Thank you for your purchase")
    return round((cost - sum).__abs__(),2)
def use_machine():
    current_resources = show_resources() #sets value for initial resources, to be modified by the upcoming methods
    choice = consumer_choice() # takes consumer choice
    #print(f"Choice: {choice}")
    drink_cost = choice[3]
    #print(f"Drink cost: {drink_cost}")
    choice.pop()
    #print(choice)

    if check_ingredients(choice,current_resources): #checks if there are enough ingredients
        print("Enough Resources Checked")
        change = take_money(drink_cost)
        print(f"Your change is {change}")
    else:
        print("Not Enough Ingredients Sorry")
use_machine()





