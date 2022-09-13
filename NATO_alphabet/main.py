student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

game_on = True
while game_on:
    user_word = (input("Which word do you want to spell? ")).upper()
    try:
        word_list = [alphabet_dict[letter] for letter in user_word]
        print(word_list)
        game_on = False
    except KeyError:
        print("Sorry, only letters in the alphabet")

