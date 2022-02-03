import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer_number, attempts):
    if guess == answer_number:
        print(f"You got it! The answer is {answer_number}.")        
    elif guess < answer_number:
        print(f"Too low, guess again.")
        return attempts - 1        
    elif guess > answer_number:
        print(f"Too high, guess again.")
        return attempts - 1        
    else:
        print("Please input an integer.")

def set_difficulty():    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        return HARD_LEVEL_TURNS
    else:
        print("Error in your input.")


logo = """
 _____                     _               _____                      
|  __ \                   (_)             |  __ \                     
| |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ 
| | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ |
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                    __/ |                             
                                   |___/                              

"""
def game():
    print(logo)
    print('Welcome to the Guessing Game')
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    answer_number = random.randint(1, 100)
    print(f"Psst, the number is {answer_number}")

    attempts = set_difficulty()
    guess = 0

    while guess != answer_number:
        if attempts == 0:
            return print("You've run out of guesses. Game over")

        print(f"You have {attempts} remaining to guess the number.")

        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, answer_number, attempts)       

game()


# correct_input = False
# while not correct_input:
#     difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if difficulty == 'easy':
#         attempts = 10
#         correct_input = True
#     elif difficulty == 'hard':
#         attempts = 5
#         correct_input = True
#     else:
#         print("Error in your input.")


# is_right = False

# while not is_right:
#     print(f'You have {attempts} guesses remaining.')
#     guess = int(input("Make a guess: "))

#     if guess == answer_number:
#         print(f"You got it! The answer is {answer_number}.")
#         is_right = True
#     elif guess < answer_number:
#         print(f"Too low, guess again.")
#         attempts = attempts - 1
#     elif guess > answer_number:
#         print(f"Too high, guess again.")
#         attempts = attempts - 1
#     else:
#         print("Please input an integer.")
    
#     if attempts == 0:
#         print("You've run out of guesses, you lose.")
#         is_right = True