import turtle
import pandas

state_data = pandas.read_csv("50_states.csv")
states = state_data.state.to_list()

# checked the actual size of the pic
WIDTH = 725
HEIGHT = 491
screen = turtle.Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_countries = []

while len(guessed_countries) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_countries)}/50 States correct", prompt="Give another state name: ").title()
    if user_answer == "Exit":
        break
    if user_answer in states:
        guessed_countries.append(user_answer)
        country_data = state_data[state_data.state == user_answer]
        country = turtle.Turtle()
        country.hideturtle()
        country.penup()
        country.goto(int(country_data.x), int(country_data.y))
        country.write(user_answer, move=False, align="center", font=("Arial", 12, "normal"))

# states to learn
states_to_learn = [state for state in states if state not in guessed_countries]
# for state in states:
#     if states not in guessed_countries:
#         states_to_learn.append(state)

# with open("states_to_learn.txt", mode="w") as file:
#     file.write(f"{states_to_learn}")

new_states_data = pandas.DataFrame(states_to_learn)
new_states_data.to_csv("states_to_learn.csv")

def get_mouse_click_coord(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coord)
turtle.mainloop()
