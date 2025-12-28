from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=500)

x = -230
y = -100
turtles = []

user_bet = screen.textinput(title="Make you bet", prompt="Which turtle is going to win the race?").lower()

for color in colors:
    tim = Turtle("turtle")
    tim.color(color)
    tim.penup()
    tim.goto(x,y)
    turtles.append(tim)
    y+=40

game_on = True

while game_on:
    for tim in turtles:
        tim.fd(random.randint(0, 10))
        if tim.xcor() > 230:
            winner = tim.pencolor()
            game_on = False
            if(winner == user_bet):
                print(f"You Won. {winner} wins the race" )
            else:
                print(f"You lose. {winner} wins the race")
            break
    
screen.exitonclick()