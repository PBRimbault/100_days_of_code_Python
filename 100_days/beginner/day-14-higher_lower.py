from os import name
from day_14_data import data
from day_14_art import logo, vs
import random

from os import system, name

def clear():

    if name == 'nt':
        _ = system('cls')

# ### MY SOLUTION ###

# person_A = random.choice(data)

# score = 0
# is_right = True

# while is_right:

#     clear()

#     print(logo)

#     person_B = random.choice(data)

#     print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}")
#     print(vs)
#     print(f"Compare B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}")

#     chosen_person = input("Who has more followers? Type 'A' or 'B': ").lower()

#     if person_A['follower_count'] > person_B['follower_count']:
#         correct_answer = 'a'
#     else:
#         correct_answer = 'b'

#     if chosen_person == correct_answer:
#         score = score + 1
#         print(f"Correct answer! Your score is {score}")
#         person_A = person_B
#         if input("Would you like to continue playing? Type 'y' or 'n': ").lower() == 'n':
#             is_right = False
#     else:
#         print(f"Wrong answer. Your high score was {score}")
#         is_right = False

### ANGELA'S SOLUTION ###

def format_data(account):
    '''Format account data and returns the printable format'''
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):    
    ''' Take the user guess and follower counts and returns if they got it right.'''
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:

    # Make the game repeatable, taking previous B and using it as A
    # Generate a randomly selected account from the game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    clear()
    print(logo)

    # Give user feedback on their guess
    # Keep score of user

    if is_correct:
        score = score + 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")

