# Randomisation and Python Lists
import random

# Exercise 1 - Virtual coin toss 
print("This is a virtual coin toss. The coin landed on ....")
random_number = random.randint(0, 1)

if random_number == 1:
    print("Heads.")
elif random_number == 0:
    print("Tails.")
else:
    print("Error")

# Exercise 2 - Name Picker
# Write a program which will select a random name from a list of names

# Don't change code below this line
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# Don't change code above this line

# Write your code below this line
upper = len(names) - 1
random_index = random.randint(0, upper)
payer = names[random_index]
print(f"{payer} has been chosen to pay the bill.")