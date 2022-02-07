# Print report
## Report has all the remaining resources in the coffee machine

# Check that resources are sufficient to make the cup of coffee requested
## Check against recipe and report abck on the resources that are not sufficient

# Ability to process coins inserted by the user and return the correct amount of change
## Ask how many quarters($0.25), dimes($0.10), nickles($0.05) and/or pennies($0.01) are to be inserted

# Check that the transaction was successful - basically has the user inserted enough money

# Deduct resources from the inventory

import this


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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

