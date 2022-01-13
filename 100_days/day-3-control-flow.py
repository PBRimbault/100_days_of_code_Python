# Control Flow
# Exercise 1 - Height Checker
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    
    age = int(input("What is yout age? "))
    if age <+ 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
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