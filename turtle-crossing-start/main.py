import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key='Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move()

    if player.is_at_finish_line():
        player.starting_position()
        car_manager.level_up()
        score.update_score()

    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            score.game_over()
            game_is_on = False

    screen.update()


screen.exitonclick()
