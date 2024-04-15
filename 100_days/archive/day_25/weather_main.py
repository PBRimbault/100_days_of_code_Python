
# with open("weather_data.csv", "r") as data_file:
#     data = data_file.read().readlines()
#     print(data)

# import csv


# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(data["temp"])

# date_dict = data.to_dict()
# print(date_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)

# Get Data in Columns
# print(data['temp'].mean())
# print(data['temp'].max())

# Get Data in Row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((9 / 5 ) * int(monday.temp) + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")