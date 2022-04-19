from turtle import Turtle, Screen
import turtle
import colorgram
import random

turtle.colormode(255) #Sets the colormode for RGB

def tuple_colors(color):#Function to extract colors in a picture
    my_color_list = []
    for rgb_colors in color:
        my_color_tuple = (rgb_colors.rgb.r,rgb_colors.rgb.g,rgb_colors.rgb.b)
        my_color_list.append(my_color_tuple)
    return my_color_list



colors = colorgram.extract('painting_img.jpg', 30)
print(tuple_colors(colors))

new_turtle = turtle
number_of_dots = 100

new_turtle.penup()
new_turtle.setheading(270)
new_turtle.forward(300)
new_turtle.setheading(0)

generated_colors = tuple_colors(colors)

for dot_count in range(1,number_of_dots+1):
    new_turtle.dot(70,random.choice(generated_colors)) #Creates the dots using random colors
    new_turtle.forward(50)

    if dot_count %10==0:
        new_turtle.setheading(90)
        new_turtle.forward(50)
        new_turtle.setheading(180)
        new_turtle.forward(500)
        new_turtle.setheading(0)

screen = Screen()
screen.exitonclick()