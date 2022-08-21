import art
alphabet = art.alphabet

print(art.logo)

def encrypt (text, shift):
    letters = []
    encoded_letters = []
    for letter in text:
        if letter in alphabet:
            letters.append(letter)
            index = alphabet.index(letter)
            if shift >= (len(alphabet) - index):
                new_index = shift - (len(alphabet) - index)
                encoded_letters.append(alphabet[new_index])
            else:
                encoded_letters.append(alphabet[index + shift])
    print(letters)
    encoded_text=""
    print(f"The encoded text is {encoded_text.join(encoded_letters)}.")

def decrypt (text, shift):
    encoded_letters = []
    decoded_letters = []
    for letter in text:
        if letter in alphabet:
            encoded_letters.append(letter)
            index = alphabet.index(letter)            
            if shift >= index:
                new_index = index - shift 
                decoded_letters.append(alphabet[new_index])
            else:
                decoded_letters.append(alphabet[index - shift])
                
    print(encoded_letters)
    decoded_text=""
    print(f"The decoded text is {decoded_text.join(decoded_letters)}.")

# my function, not as elegant as theirs, but whatever
def caesar(direction, text, shift):
    coded_text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                if shift%len(alphabet) >= (len(alphabet) - index):
                    new_index = shift%len(alphabet) - (len(alphabet) - index)
                    coded_text += alphabet[new_index]
                else:
                    coded_text += alphabet[index + shift%len(alphabet)]
            elif direction == "decode":
                if shift%len(alphabet) >= index:
                    new_index = index - shift%len(alphabet) 
                    coded_text += alphabet[new_index]
                else:
                    coded_text += alphabet[index - shift%len(alphabet)]
            else:
                while direction != "encode" and direction != "decode":
                    direction = input("Please give a valid option for direction:\n")
        else:
            coded_text += letter
    print(f"The {direction}d text is '{coded_text}'.")

def get_var (direction):
    while direction != "encode" and direction != "decode":
        direction = input("Please give a valid option:\n")
    if direction == "encode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            encrypt(text, shift)
    elif direction == "decode":
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            decrypt(text, shift)

# only giving direction initially
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# get_var(direction=direction)

# giving all parameters initially
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# caesar(direction=direction, text=text, shift=shift)

play = True
while play == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction=direction, text=text, shift=shift)
    option = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if option == "yes":
        play = True
    elif option == "no":
        play = False
        print("Bye bye now!")
    else:
        option = input("Please give a valid option. Type 'yes' if you want to go again. Otherwise type 'no'.\n")
