# Functions with outputs

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"
#     formated_f_name = (f_name.title())
#     formated_l_name = (l_name.title())
#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# # Coding Exercise 1 - Days in Month

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# def days_in_month(input_year, input_month):
#     if len(str(input_year)) < 4:
#         return "Invalid year"
#     if input_month > 12 or input_month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(input_year) and input_month == 2:
#         return '29'
#     return month_days[input_month - 1]

# # Do not change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Calculator Challenge

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    "/" : divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue == True:       

        operation_symbol = input("Pick another operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_answer = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start the calculator again: ")

        if  continue_answer == 'y':
            num1 = answer
        elif continue_answer == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()