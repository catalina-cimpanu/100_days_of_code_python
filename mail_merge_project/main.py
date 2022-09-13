with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
names_file.close()
print(names)

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    model_letter = starting_letter.read()
    for name in names:
        name = name.strip()
        letter = model_letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as new_file:
            new_file.write(letter)
        new_file.close()
