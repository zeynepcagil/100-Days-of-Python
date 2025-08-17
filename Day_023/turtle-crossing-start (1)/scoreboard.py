from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.write(f"Level : {self.level}",font=FONT)


    def increase_level(self):
        self.level+=1
    def update_score_board(self):
        self.clear()
        self.write(f"Level : {self.level}", font=FONT)
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER ", font=FONT)