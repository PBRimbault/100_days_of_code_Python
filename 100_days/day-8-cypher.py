# Day 8 - Buildign a Caesar Cypher
# input_name = input("What is your name? ")

# def greet(name):
#     print(f'Hello {name}')
#     print(f'How do you do {name}?')
#     print(f"Isn't the weather nice today, {name}?")

# greet(input_name)

# input_name = input("What is your name? ")
# input_location = input(f"Where do you live {input_name}? ")

# def greet_with(name, location):
#     print(f'Hello {name}')
#     print(f'How do you do {name}?')
#     print(f"What is it like in {location}?")

# greet_with(location = input_location, name = input_name)

# # Coding Challenge 1
# # Write your code below this line

# import math

# def paint_calc(height, width, cover):
#     number_cans = math.ceil((height * width) / cover)
#     print(f"The number of cans required is {number_cans}")

# # Write your code above this line

# # Don't change the code below
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height = test_h, width = test_w, cover = coverage)

# # Coding Challenge 2
# # Write your code below this line

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print(f"{number} is a prime number")
#     else:
#         print(f"{number} is a composite number")        

# # Write your code above this line

# # Don't change the code below
# n = int(input("Check this number: "))
# prime_checker(number = n)

# Coding Project - Caesar Cipher
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.

print(logo)

    #TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
    #e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
    #If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
    #Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
restart = 'yes'

while restart == 'yes':

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = (int(input("Type the shift number:\n"))) % 26

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    print("Would you like to restart Caesar Cipher?")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no' ")

print('Goodbye!')