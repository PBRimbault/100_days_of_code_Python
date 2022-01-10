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