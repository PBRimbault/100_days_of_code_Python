####TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
PLACEHOLDER = "[name]"


with open("./Mail Merge/Input/Names/invited_names.txt", "r") as name_file:
    name_list = name_file.read().splitlines()

for name in name_list:
    with open("./Mail Merge/Input/Letters/starting_letter.txt", "r") as contents:
        starting_letter = contents.read()
    
    final_letter = starting_letter.replace(PLACEHOLDER, name)
    
    with open(f"./Mail Merge/Output/ReadyToSend/letter_for_{name.lower()}.txt", "x") as final_file:
        final_file.write(final_letter)

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp