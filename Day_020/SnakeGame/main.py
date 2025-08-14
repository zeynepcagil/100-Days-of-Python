from turtle import Turtle,Screen
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)
starting_positions=[(0,0),(-20,0),(-40,0)]
segments=[]

def move_right():
    snake.forward(10)
def move_left():
    snake.forward(-10)
def move_forward(snake):
    snake.forward(-10)
def move_backward(snake):
    snake.forward(-10)


for positions in starting_positions:
    snake=Turtle(shape="square")
    snake.penup()
    snake.goto(positions)
    segments.append(snake)
screen.update()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)













screen.exitonclick()