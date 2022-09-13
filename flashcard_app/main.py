from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
GREEN = "#91C2AF"

# ------------------- READ WORDS ---------------------#

try:
    words_df = pandas.read_csv("./data/words_to_learn.csv")
    if words_df.empty:
        raise Exception("File is empty")
except:
    all_words = pandas.read_csv("./data/french_words.csv")
    words = {row.French: row.English for (index, row) in all_words.iterrows()}
    # words = all_words.to_dict(orient="records")
else:
    # words = words_df.to_dict(orient="records")
    words = {row.French: row.English for (index, row) in words_df.iterrows()}


# ---------------------- CARD FUNCTIONS ----------------#
word = None
translation = None

def generate_card():
    global word, translation, words
    if words:
        word = random.choice(list(words.keys()))
        translation = words[word]
        displayed_language.config(text="French", bg="white")
        displayed_word.config(text=f"{word}", bg="white")
        card.itemconfig(card_image, image=card_front_img)
    else:
        displayed_language.config(text="You learnt all words", bg="white")
        displayed_word.config(text="Bravo!", bg="white")

def flip_card():
    if displayed_language.cget("text") == "French":
        displayed_language.config(text="English", bg=GREEN)
        displayed_word.config(text=f"{translation}", bg=GREEN)
        card.itemconfig(card_image, image=card_back_img)
    else:
        displayed_language.config(text="French", bg="white")
        displayed_word.config(text=f"{word}", bg="white")
        card.config(bg=BACKGROUND_COLOR)
        card.itemconfig(card_image, image=card_front_img)

# -------------------- SAVE PROGRESS ------------------- #

def learn_word():
    global word
    words.pop(word)
    print(words)
    # data = pandas.DataFrame.from_dict(words, orient='index', columns=['French'])
    data = pandas.DataFrame(list(words.items()), columns=['French', 'English'])
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_card()


# ------------------------ GUI ------------------------- #
window = Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.after(3000, func=flip_card)

# Card sides
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 263, image=card_front_img)
card.grid(column=0, row=0, columnspan=3, rowspan=2)

displayed_language = Label(text="French", bg="white", font=("Ariel", 40, "italic"))
displayed_language.grid(column=0, row=0, columnspan=3, pady=(100, 0))

displayed_word = Label(text="Word", bg="white", font=("Ariel", 60, "bold") )
displayed_word.grid(column=0, row=1, columnspan=3, pady=(0, 100))

generate_card()

# Buttons
correct_img = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_img, command=learn_word, highlightthickness=0, borderwidth=0)
correct_button.grid(column=2, row=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, command=generate_card, highlightthickness=0, borderwidth=0)
wrong_button.grid(column=0, row=2)

flip_button = Button(text="Flip", command=flip_card, highlightthickness=0, font=("Ariel", 16, "bold"),
                     relief="flat")
flip_button.grid(column=1, row=2)

window.mainloop()
