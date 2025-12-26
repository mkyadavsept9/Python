import colorgram
import turtle
import random

colors = colorgram.extract('image.jpeg', 20)
random_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    random_colors.append((r,g,b))

x = -200
y = -200

turtle.colormode(255)

tim = turtle.Turtle()
tim.penup()
tim.goto(x, y)
tim.pendown()

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(random_colors))
        tim.penup()
        tim.fd(40)
        tim.pendown()
    tim.penup()
    y += 40
    tim.goto(x, y)
    tim.pendown()

screen = turtle.Screen()
screen.exitonclick()
    