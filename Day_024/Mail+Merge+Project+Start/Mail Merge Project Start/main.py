#TODO: Create a letter using starting_letter.txt
letter = open("Input/Letters/starting_letter.txt", mode="r+")
names = open("Input/Names/invited_names.txt", mode="r+")

name_list = []
for name in names:
    name_list.append(name.strip())
print(name_list)

letter_content = letter.read()

letter.close()
names.close()

for name in name_list:

    file_name = f"Output/ReadyToSend/letter_for_{name}.txt"

    new_content = letter_content.replace("[name]", name)


    with open(file_name, "w") as new_letter:
        new_letter.write(new_content)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp