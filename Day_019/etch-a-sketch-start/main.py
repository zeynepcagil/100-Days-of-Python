from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.forward(-10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def clock_wise():
    tim.circle(20,15)
def turn():
    tim.right(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="c",fun=clear)
screen.onkey(key="d",fun=clock_wise)
screen.onkey(key="a",fun=turn)
screen.exitonclick()
