# Exercise 1 - Average Height

# Don't change the code below
student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# Don't change the code above

sum = 0
count = 0

for height in student_heights:
    sum += height
    count += 1

average = round(sum / count, 0)
print(f"The average student height is {average}.")

# Exercise 2 - Highest Score

# Don't change the code below
student_scores = input("Input a list of student scores\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# Don't change the code above

high_score = 0

for score in student_scores:
    if high_score < score:
        high_score = score

print(f"The highest score in the class is: {high_score}")

# Exercise 3 - Add all the even numbers in range

# Don't change the code below

# Don't change the code above

sum = 0

for number in range(1, 101):
    if (number % 2) == 0:
        sum = sum + number

print(f"The sum of the even numbers in the range is: {sum}")

# Exercise 4 - FizzBuzz Game
# Print each number from 1 to 100
# If number is divisible by 3, print Fizz instead of the number
# If number is divisible by 5, print Buzz instead of the number
# If number is divisible by both 3 and 5, print FizzBuzz instead

# Don't change the code below

# Don't change the code above

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

code_letters = []
for i in range(nr_letters):
    random_letter = letters[random.randint(0, len(letters) - 1)]
    code_letters.append(random_letter)

code_numbers = []
for i in range(nr_numbers):
    random_number = numbers[random.randint(0, len(numbers) - 1)]
    code_numbers.append(random_number)

code_symbols = []
for i in range(nr_symbols):
    random_symbol = symbols[random.randint(0, len(symbols) - 1)]
    code_symbols.append(random_symbol)

code_characters = code_letters + code_numbers + code_symbols
code_str = ''

for i in range(len(code_characters)):
    code_str += code_characters[random.randint(0, len(code_characters) - 1)]

print(f"Here is your password: {code_str}")