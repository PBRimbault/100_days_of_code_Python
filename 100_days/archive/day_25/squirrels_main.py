data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# fur_count = data['Primary Fur Color'].value_counts()
# fur_count.to_csv("fur_count.csv")

gray_fur = 0
cinnamon_fur = 0
black_fur = 0

for value in data['Primary Fur Color']:
    if value == "Gray":
        gray_fur += 1
    if value == "Cinnamon":
        cinnamon_fur += 1
    if value == "Black":
        black_fur += 1

fur_dict = {
    "Fur Color": ["grey", "cinnamon", "black"],
    "Count": [gray_fur, cinnamon_fur, black_fur]
}

data_dict = pandas.DataFrame(fur_dict)
print(data_dict)
data_dict.to_csv("fur_count.csv")