import turtle
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = turtle.Turtle()
tim.speed(0)
tim.pensize(2)

for _ in range(36):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(10)

screen = turtle.Screen()
screen.exitonclick()