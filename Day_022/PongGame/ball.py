from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.xmove=10
        self.ymove=10



    def move(self):
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.penup()
        self.goto(new_x,new_y)

    def change_balance(self):
        self.ymove=-self.ymove
    def change(self):

        self.xmove=-self.xmove
    def reset_position(self):
        self.goto(0,0)
        self.change()
        self.move()