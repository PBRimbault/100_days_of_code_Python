with open("C:/Users/Patrick/Documents/GitHub/100_days_of_code_Python/100_days/day_24/new_file.txt", mode="w") as file:
    file.write("This is a new file.\nWith new text.")

with open("C:/Users/Patrick/Documents/GitHub/100_days_of_code_Python/100_days/day_24/new_file.txt") as file:
    contents = file.read()
    print(contents)