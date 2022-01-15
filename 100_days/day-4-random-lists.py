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

# Exercise 2 - Treasure Map

# Don't change the code below
row1 = ['🙂', '🙂', '🙂']
row2 = ['🙂', '🙂', '🙂']
row3 = ['🙂', '🙂', '🙂']
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Specify column number then row number. ")
# Don't change code above this line

# Write your code below this line
column = int(position[0])
row = int(position[1])
map[row - 1][column - 1] = 'X'
print(f"{row1}\n{row2}\n{row3}")

# Challenge - Rock, Paper, Scissors game

# Don't change the code below
import random

choice = (input("What do you choose? Rock, Paper or Scissors? ")).lower()

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Don't change code above this line

# Write your code below this line
if choice == 'rock':
    choice = 0
elif choice == 'paper':
    choice = 1
elif choice == 'scissors':
    choice = 2
else:
    print("Error.")

computer_choice = random.randint(0, 2)

if choice == 0:
    print(f"You chose:\n\n{rock}")
    if computer_choice == 0:
        print(f"Computer chose:\n\n{rock}")
        print("Game tied.")
    elif computer_choice == 1:
        print(f"Computer chose:\n\n{paper}")
        print("You lose.")
    elif computer_choice == 2:
        print(f"Computer chose:\n\n{scissors}")
        print("You win.")
    else:
        print("Error.")

if choice == 1:
    print(f"You chose:\n\n{paper}")
    if computer_choice == 0:
        print(f"Computer chose:\n\n{rock}")
        print("You win.")
    elif computer_choice == 1:
        print(f"Computer chose:\n\n{paper}")
        print("Game tied.")
    elif computer_choice == 2:
        print(f"Computer chose:\n\n{scissors}")
        print("You lose.")
    else:
        print("Error.")

if choice == 3:
    print(f"You chose:\n\n{scissors}")
    if computer_choice == 0:
        print(f"Computer chose:\n\n{rock}")
        print("You lose.")
    elif computer_choice == 1:
        print(f"Computer chose:\n\n{paper}")
        print("You win.")
    elif computer_choice == 2:
        print(f"Computer chose:\n\n{scissors}")
        print("Game tied.")
    else:
        print("Error.")
