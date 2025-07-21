###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle,Screen

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

# Example
color = (255, 0, 0)
hex_color = rgb_to_hex(color)
print(hex_color)
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)

color_list=[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
color_name=[]
for color in color_list:
    hex_color=rgb_to_hex(color)
    color_name.append(hex_color)


zeynep_turtle=Turtle()

for _ in range(1,30):
    zeynep_turtle.hideturtle()
    zeynep_turtle.dot(20, color_name[_])
    zeynep_turtle.penup()
    zeynep_turtle.forward(50)
    zeynep_turtle.pendown()

    if _ % 10 == 0:
        zeynep_turtle.penup()
        zeynep_turtle.setheading(90)
        zeynep_turtle.forward(100)
        zeynep_turtle.setheading(180)
        zeynep_turtle.forward(500)
        zeynep_turtle.setheading(0)
   
screen=Screen()
screen.exitonclick()
