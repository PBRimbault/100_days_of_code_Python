# # FileNotFound Error
# try:
#     file = open('a_file.txt')
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Created a file")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is an error that I made up")



# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["not_a_key"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit_list[4]

# # TypeError
# text = "abc"
# print(text + 5)

# Raising your own errors
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)