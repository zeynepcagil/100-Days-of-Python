import pandas as pd
from turtle import Screen,Turtle

screen=Screen()
turtle=Turtle()
screen.title("U.S. State Game")

image="blank_states_img.gif"
path="50_states.csv"

all_states=pd.read_csv(path)

state_list=(list(all_states["state"]))
coor_x=(all_states["x"])
coor_y=(all_states["y"])
coor_list=list(zip(coor_x,coor_y))
print(coor_list)
screen.addshape(image)
turtle.shape(image)

game_on=True

while game_on:
    answer_state = screen.textinput("Guess the state", "What's another state's name")
    if answer_state.lower() in [s.lower() for s in state_list]:
        abc = Turtle()

        abc.penup()
        abc.hideturtle()
        abc.goto(coor_list[state_list.index(answer_state.title())])
        abc.write(arg=answer_state.title(), font=("Arial", 8, "normal"))

    else:
        print("nein")

screen.exitonclick()






