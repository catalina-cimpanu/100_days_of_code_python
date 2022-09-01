import colorgram
import random
import turtle as t
t.colormode(255)

def get_colors(image_name):
    colors = colorgram.extract(image_name, 30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors


def paint_hirst():
    screen = t.Screen()
    screen.setup(width=850, height=850)

    tim = t.Turtle()
    tim.speed(0)
    tim.hideturtle()
    tim.penup()
    tim.setposition(-300,-300)

    colors = get_colors('Ellipticine.jpeg')

    for i in range(0, 10):
        for j in range(0,10):
            # color = colors[i+j]
            color = random.choice(colors)
            tim.pendown()
            tim.dot(20, color)
            tim.penup()
            tim.forward(70)
        if i % 2 == 0:
            tim.left(90)
            tim.forward(70)
            tim.left(90)
            tim.forward(70)
        else:
            tim.right(90)
            tim.forward(70)
            tim.right(90)
            tim.forward(70)

    screen.exitonclick()


paint_hirst()
