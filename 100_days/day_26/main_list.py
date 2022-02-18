with open("file1.txt", "r") as name_file:
    file1_list = name_file.read().splitlines()

with open("file2.txt", "r") as name_file:
    file2_list = name_file.read().splitlines()

result = [int(n) for n in file2_list if n in file1_list]

print(result)