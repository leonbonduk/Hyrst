# import colorgram
#
# colours = colorgram.extract('image.jpg', 30)
#
# rgb_colours = []
# for col in colours:
#     red = col.rgb.r
#     green = col.rgb.g
#     blue = col.rgb.b
#     new_colour = (red, green, blue)
#     rgb_colours.append(new_colour)
#
# # print(rgb_colours)

import turtle as t
import random

colour_list = [(235, 224, 84), (113, 179, 212), (213, 158, 111), (205, 5, 68), (235, 50, 128), (195, 74, 16), (194, 165, 12), (13, 22, 60), (31, 103, 167), (233, 225, 4), (28, 191, 119), (215, 135, 177), (17, 28, 173), (203, 31, 129), (230, 166, 199), (12, 184, 214), (119, 192, 162), (61, 22, 9), (35, 136, 76), (139, 219, 202), (9, 48, 26), (104, 92, 211), (188, 16, 5), (128, 218, 232), (238, 66, 36), (64, 12, 37)]

turt = t.Turtle()
screen = t.Screen()
turt.pensize(20)
screen.colormode(255)

turt.penup()
screen_width = screen.screensize()[0]
screen_height = screen.screensize()[1]
x_coord = -screen_width/2 +20
y_coord = -screen_height/2 +20
turt.setx(x_coord)
turt.sety(y_coord)

for rows in range (0,10):
    for cols in range(0,10):
        turt.pendown()
        t_color = random.choice(colour_list)
        turt.pencolor(t_color)
        turt.dot(20)
        turt.penup()
        turt.forward(50)
    turt.left(90)
    turt.forward(50)
    turt.left(90)
    turt.forward(500)
    turt.right(180)

screen.exitonclick()