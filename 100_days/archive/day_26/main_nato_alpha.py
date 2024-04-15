# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
df = pandas.read_csv("nato_phonetic_alphabet.csv")


# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# print(df)

nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Input your word for translation: ").upper()

nato_list = [nato_dict[letter] for letter in input_word]

print(nato_list)