# programming_dictionary = {
#     "Bug" : "An error in a progrm that prevernts the proram from running as expected.", 
#     "Function" : "A piece of code that you can easily call over and over again.",
# }

# # Retrieving items from dictionary.
# print(programming_dictionary["Bug"])

# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

# # # Create an empty dictionary
# # empty_dictionary = {}

# # # Wipe and existing dictionary
# # programming_dictionary = {}

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Day 9 Coding Exercise 1 - Grading Program
# student_scores = {
#     "Harry" : 81,
#     "Ron" : 78,
#     "Hermione" : 99,
#     "Draco" : 74,
#     "Neville" : 62,
# }

# # To do 1 - Create and empty dictionary called student_grades
# student_grades = {}

# # To do 2 - Write your code below to add the grades to student_grades
# for student in student_scores:
#     if student_scores[student] <= 70:
#         student_grades[student] = "Fail"
#     elif student_scores[student] <= 80:
#         student_grades[student] = "Acceptable"
#     elif student_scores[student] <= 90:
#         student_grades[student] = "Exceeds Expectations"
#     else:
#         student_grades[student] = "Outstanding"

# print(student_grades)

# # Day 9 Coding Exercise 2 - Grading Program

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(new_country, num_visits, cities_visited):
    
#     travel_log.append({
#         "country" : new_country, 
#         "visits" : num_visits,
#         "cities" : cities_visited,
#         })

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Coding Challenge - Silent Auction

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

from os import system, name

def clear():

    if name == 'nt':
        _ = system('cls')

def get_bid(name, bid_amount):
    bids[name] = bid_amount

clear()

print(logo)
print("Welcome to the secrete auction program")

bids = {}

add_bid = 'yes'

while add_bid == 'yes':
    
    bidder_name = input("What is your name?: ")
    bidder_price = int(input("What is your bid?: $"))

    get_bid(name=bidder_name, bid_amount=bidder_price)

    add_bid = input("Are there any other bidders? Type 'yes' or 'no' ")

    clear()

max_bid = 0
winner = ''

for bidder in bids:
    if bids[bidder] > max_bid:
        max_bid = bids[bidder]
        winner = bidder

print(f"The winning bid was ${max_bid} by {winner}")