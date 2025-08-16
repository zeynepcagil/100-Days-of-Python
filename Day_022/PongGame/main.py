# main.py
from turtle import Screen
from user import User
from ball import Ball
import time
from score_board import Score_Board

score_board_1=Score_Board((100,250))
score_board_2=Score_Board((-100,250))

ball=Ball()
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

user1 = User(-350, 0)  # solda
user2 = User(350, 0)   # sağda

# Kontroller
screen.listen()
screen.onkey(user1.up, "w")
screen.onkey(user1.down, "s")
screen.onkey(user2.up, "Up")
screen.onkey(user2.down, "Down")

# Oyun döngüsü
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_balance()
    if ball.distance(user1)<50 and ball.xcor()<-320 or ball.distance(user2)<50 and ball.xcor()>320 :
        ball.change()
    if ball.xcor()<-380:
        score_board_1.calculate_Score()
        score_board_1.update_score_board()
        ball.reset_position()
    if ball.xcor() > 380:
        score_board_2.calculate_Score()
        score_board_2.update_score_board()
        ball.reset_position()


screen.exitonclick()
