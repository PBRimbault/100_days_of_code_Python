# Data types

# String
# Subscripting with [x] prints out the character at x from left
print("Hello"[2])

# Concatenating strings is easy
print("123" + "345")

# Integer
print(123 + 345)

# Float
3.14159

# Boolean
True
False

# Type errors and type casting
num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.") # will fail! Giving typeError
# Need to typecast integer to string
print("Your name has " + str(num_char) + " characters.")

# Code Challenge # 1
# Write a program that adds the digits in a 2 digit number. e.g. input is 35, output = 3 + 5 = 8

# Don't change the code below
two_digit_number = input("Type a two digit number: ")
# Don't change the code above

#################################
# Write your code below this line
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(int(first_digit) + int(second_digit))

# Code Challenge # 2
# Write a program that calculates your BMI based on input height and weight, BMI = weight/height

# Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# Don't change the code above

#################################
# Write your code below this line
float_height = float(height)
float_weight = float(weight)
bmi = float_weight / float_height ** 2
print(round(bmi, 2))

# Code Challenge # 3

# Don't change the code below
age = input("What is your current age? ")
# Don't change the code above

#################################
# Write your code below this line
days_left = (90 * 365) - (int(age) * 365)
weeks_left = (90 * 52) - (int(age) * 52)
months_left = (90 * 12) - (int(age) * 12)

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} until you are 90 years old.")

# Code Challenge # 4
# Bill tip split calculator

# Don't change the code below
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $ ")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
# Don't change the code above

#################################
# Write your code below this line
amnt_due = (float(bill) * (1 + float(tip) / 100)) / int(people)
print("Each person should pay: $" + str(round(amnt_due, 2)))