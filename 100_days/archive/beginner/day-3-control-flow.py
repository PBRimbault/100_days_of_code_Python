# Control Flow
# Exercise 1 - Height Checker
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    
    age = int(input("What is yout age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Mid-life crisis tickets are $0.")
        bill = 0
    else:
        print("Adult tickets are $12.")
        bill = 12

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your bill is {bill} please.")
else:
    print("You are too short, you cannot continue")

# Code Challenge 1
# Write a program that works out if a given number is odd or even

# Don't change the code below
number = int(input("Which number do you want to check? "))
# Don't change the code above

# Write your code below this line
remainder = number % 2

if remainder == 1:
    print("This number is false")
else:
    print("This number is even")

# Code Challenge 2
# BMI Calculator 2.0 - Write a program that interprets the BMI based on a user's weight and height
# Under 18.5 they are underweight
# Over 18.5 but under 25 they have a normal weight
# Over 25 but below 30 they are overweight
# Over 30 but below 35 they are obese
# Over 35 they are clinically obese

# Don't change the code below
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# Don't change the code above

bmi = int(weight / height ** 2)

if bmi <= 18.5:
    print("You are underweight")
elif bmi <= 25:
    print("You have a normal weight")
elif bmi <= 30:
    print("You are overweight")
elif bmi <= 35:
    print("You are obese")
else:
    print("You are clinically obese")

# Code Challenge 3
# Write a program that works out if a given year is a leap year.
# Normal years have 365 days, leap yeras have 366 days, wih an extra day in February
# The logic is that on every year that is evenly divisble by 4,
#       except every year that is evenly divisible by 100,
#               unless the year is also evenly divisible by 400
# 2000 / 4 = 500 (Leap), 2000 / 100 = 20 (Not Leap), 2000 / 400 = 5 (Leap).
# Therefore 2000 is a leap year
# 2100 / 4 = 525 (Leap), 2100 / 100 = 21 (Not Leap), 2100 / 400 = 5.25 (Not Leap).
# Therefore 2100 is not a leap year

# Don't change the code below
year = int(input("Which year do you to check for being a leap year? "))
# Don't change the code above

# Write your code below
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")
    else:
        print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")

# Code Challenge 4
# Based on a user's order, work out their final bill

# Small pizza : $15
# Medium pizza : $20
# Large pizza : $25

# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3

# Extra cheese for any size pizza: +$1

# Don't change the code below
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L")
add_peperroni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

# Write your code below
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_peperroni == "Y": 
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# Code Challenge 5
# Love Calculator

# Don't change the code below
print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

# Write your code below this line
name1 = name1.lower()
name2 = name2.lower()

name1_count1 = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
name1_count2 = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')

name2_count1 = name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')
name2_count2 = name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

score = int(str(name1_count1 + name2_count1) + str(name1_count2 + name2_count2))

if score <= 10 or score >= 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")