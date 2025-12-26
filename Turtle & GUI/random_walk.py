import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.pensize(10)
tim.speed(0)
turtle.colormode(255)

for _ in range(100):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    direction = random.choice([0, 90, 180, 270])

    tim.pencolor((r, g, b))
    tim.setheading(direction)
    tim.forward(20)
  


screen = Screen()
screen.exitonclick()