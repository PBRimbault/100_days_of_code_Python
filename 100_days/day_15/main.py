# Print report
## Report has all the remaining resources in the coffee machine
def print_report(current_resources, current_money):
    '''This function prints the current values for resources and money'''
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${current_money}")

# Check that resources are sufficient to make the cup of coffee requested
## Check against recipe and report abck on the resources that are not sufficient

def check_resources(current_resources, drink):
    '''This function compares the resources required for the selected drink with the available resources to make that drink'''
    if current_resources['water'] < MENU[drink]['ingredients']['water']:
        print('Sorry there is not enough water')
    elif current_resources['milk'] < MENU[drink]['ingredients']['milk']:
        print('Sorry there is not enough milk')
    elif current_resources['coffee'] < MENU[drink]['ingredients']['coffee']:
        print('Sorry there is not enough coffee')
    else:
        print(f"We have enough resources for your {drink}")
    return True

# Ability to process coins inserted by the user and return the correct amount of change
## Ask how many quarters($0.25), dimes($0.10), nickles($0.05) and/or pennies($0.01) are to be inserted
def count_money():
    print("Please insert coins.")
    inserted_quarters = int(input("How many quarters?: "))
    inserted_dimes = int(input("How many dimes?: "))
    inserted_nickles = int(input("How many nickles?: "))
    inserted_dimes = int(input("How many dimes?: "))
    inserted_money = 0.25 * inserted_quarters + 0.1 * inserted_dimes + 0.05 * inserted_nickles + 0.01 * inserted_dimes
    return inserted_money

def deduct_resources(current_resources, drink):
    current_resources['water'] = current_resources['water'] - MENU[drink]['ingredients']['water']
    current_resources['coffee'] = current_resources['coffee'] - MENU[drink]['ingredients']['coffee']
    current_resources['milk'] = current_resources['milk'] - MENU[drink]['ingredients']['milk']

# Check that the transaction was successful - basically has the user inserted enough money

# Deduct resources from the inventory

MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

PROFIT = 0
SHOULD_CONTINUE = True

while SHOULD_CONTINUE:
    user_instruction = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if user_instruction == 'report':
        print_report(resources, PROFIT)
    elif user_instruction == 'off':
        SHOULD_CONTINUE = False
    elif user_instruction == 'espresso' or user_instruction == 'latte' or user_instruction == 'cappuccino':
        if check_resources(resources, user_instruction):
            drink_cost = MENU[user_instruction]['cost']
            print(f'A {user_instruction} costs ${drink_cost}.')
            user_money = count_money()
            # print(f"You have inserted {user_money}")            
            # print(f"Your drink costs {drink_cost}")
            if user_money >= drink_cost:
                change = user_money - drink_cost
                print(f'Here is your change: ${change}')
                PROFIT = PROFIT + drink_cost
                deduct_resources(resources, user_instruction)
                print(f"Thank you. Here is your {user_instruction}")
            else:
               print(f"Sorry, that's not enough money. A {user_instruction} costs ${drink_cost}. MONEY REFUNDED")