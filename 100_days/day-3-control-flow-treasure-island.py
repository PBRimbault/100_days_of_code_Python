# Day 3 Project : Treasure Island Game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'. ").lower()

if left_right == "left":
    wait_swim = input("That's the right choice! You're at a tricky river crossing. Should you wait or swim across? Type 'swim' or 'wait'. ").lower()
    if wait_swim == "wait":
        three_doors = input("You have 3 doors in front of you, a red, blue or yellow door. Which clolour do you pick? ").lower()
        if three_doors == "yellow":
            print("Well done. You win!")
        elif three_doors == "red":
            print("Game over.")
        else:
            print("Game over.")
    else:
        print("Game over.")
else:
    print("Game over.")