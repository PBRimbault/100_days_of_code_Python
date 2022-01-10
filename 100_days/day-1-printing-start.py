# input() will get user input in the console
# then, print() will print the word "Hello" and the user input
name = input("What is your name? ")
length = len(name)
print(length)

# a and b value swap using a temporary variable for a
# get input from the user
a = input("a: ")
b = input("b: ")

# the magic swap happens here
temp_a = a
a = b
b = temp_a

# print out the values
print("a: " + a)
print("b: " + b)

#1. Create a greeting for your program
print("Welcome to the Band Name Generator App!")

#2. Ask the user for the city that they grew up in.
print("What city did you grow up in?")
city = input()

#3. Ask the user for the name of their favourite pet
print("What was the name of your favourite pet?")
pet = input()

#4. Combine the city and pet names
print("Your band name could be " + city + " " + pet)