from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score_board import Score_Board

snake=Snake()
screen=Screen()
food=Food()
score_board=Score_Board()


screen.setup(600,600)
screen.bgcolor("green")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()
    if snake.head.distance(food)<10:

        food.go_random_point()
        snake.extend()
        score_board.calculate_Score()
        score_board.update_score_board()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        score_board.game_over()
        game_is_on=False

    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            score_board.game_over()
            game_is_on=False











screen.exitonclick()