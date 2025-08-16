from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.score=0
        self.update_score_board()

    def update_score_board(self):

        self.write(f"Score : {self.score}",align="center", font=  ("Arial", 16, "normal"))
    def game_over(self):

        self.goto(0,0)
        self.write(f"GAME OVER",align="center", font=  ("Arial", 16, "normal"))

    def calculate_Score(self):
        self.clear()
        self.score+=1

