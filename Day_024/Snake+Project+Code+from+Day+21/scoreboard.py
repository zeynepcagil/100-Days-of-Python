from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.bestscore=0
        with open(file="data.txt", mode="r") as file:
            self.bestscore=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score : {self.bestscore}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score>self.bestscore:
            self.bestscore=self.score
            with open(file="data.txt",mode="w") as file:
                file.write(f"{self.bestscore}")

        self.score=0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
