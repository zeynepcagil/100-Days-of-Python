from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
<<<<<<< HEAD
        self.bestscore=0
        with open(file="data.txt", mode="r") as file:
            self.bestscore=int(file.read())
        self.color("white")
        self.penup()
=======
        self.color("white")
        self.penup()
        self.best_score=0
>>>>>>> c2895e03e5f723398c541b019fdad899ffc980b3
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
<<<<<<< HEAD
        self.clear()
        self.write(f"Score: {self.score}   High Score : {self.bestscore}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score>self.bestscore:
            self.bestscore=self.score
            with open(file="data.txt",mode="w") as file:
                file.write(f"{self.bestscore}")

        self.score=0
        self.update_scoreboard()

=======
        self.write(f"Score: {self.score}  High Score ={self.best_score}", align=ALIGNMENT, font=FONT)
    def reset(self):
        if self.score>self.best_score:
            self.best_score=self.score
        self.score=0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
>>>>>>> c2895e03e5f723398c541b019fdad899ffc980b3

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
