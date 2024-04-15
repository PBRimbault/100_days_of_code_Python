# Vanilla python dictionary comprehension

# weather_c = {
#     "Monday" : 12,
#     "Tuesday" : 14,
#     "Wednesday" : 15,
#     "Thursday" : 14,
#     "Friday" : 21,
#     "Saturday" : 22,
#     "Sunday" : 24
# }

# # Write code below

# result = {day:((temp * 9/5) + 32) for (day, temp) in weather_c.items()}

# print(result)

# Dictionary comprehension using pandas DataFrames
import pandas

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Loop through a dataframe
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela"