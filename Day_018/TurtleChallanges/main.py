from turtle import Turtle,Screen
import random

colors=["pink","yellow","brown","red","blue","cyan","green","gray"]
directions=[0,90,180,270]

#Turtle Challanges 1 :Draw a square
challange1=False
challange2=False
challange3=False
challange4=False
challange5=True
zeynep_turtle=Turtle()
zeynep_turtle.shape("turtle")
zeynep_turtle.color("pink")
while challange1:
    zeynep_turtle.forward(100)
    zeynep_turtle.right(90)
    zeynep_turtle.forward(100)
    zeynep_turtle.right(90)
    zeynep_turtle.forward(100)
    zeynep_turtle.right(90)
    zeynep_turtle.forward(100)
#Turtle Challanges 2 :Draw a dashed line
while challange2:
    for _ in range(20):
        zeynep_turtle.forward(10)
        zeynep_turtle.penup()
        zeynep_turtle.forward(10)
        zeynep_turtle.pendown()
#Turtle Challanges 3 :Drawing different shapes
while challange3:
    i=3
    for i in range(i,11,1):
        zeynep_turtle.color(random.choice(colors))
        for _ in range(i):

            zeynep_turtle.forward(40)
            zeynep_turtle.right(360/i)

    challange3=False
#Turtle Challanges 4 :Random walk
while challange4:
    zeynep_turtle.speed(10)
    n=1
    for _ in range(100):
        zeynep_turtle.color(random.choice(colors))
        zeynep_turtle.pensize(n)

        zeynep_turtle.forward(random.randint(20,60))
        zeynep_turtle.setheading(random.choice(directions))
        n+=1
    challange4=False
#Turtle Challanges 5 : Spirograph
while challange5:
    zeynep_turtle.speed(30)
    for _ in range(36):
        zeynep_turtle.color(random.choice(colors))
        zeynep_turtle.circle(100)
        zeynep_turtle.left(10)
    challange5=False


screen=Screen()
screen.exitonclick()