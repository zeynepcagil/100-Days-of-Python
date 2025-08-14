import random
from turtle import Turtle, Screen

is_race_on=False
screen = Screen()
screen.setup(500,400)
user_bet=screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")
colors= [ "red","orange","yellow","green","blue","purple"]
n=0
all_turtles=[]
for turtle_index in range(0,6):

    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-200,180+n)
    n-=60
    all_turtles.append(tim)
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in all_turtles:
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
        turtle_x=turtle.xcor()
        if turtle_x>250:
            is_race_on = False
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print("You win")
            else:
                print(f"You lose, you choose {user_bet}, the winner is {winning_color}.")


screen.exitonclick()