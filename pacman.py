from turtle import Turtle,Screen, title
from food import Food
from scoreboard import scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("bonk")
snake=Turtle("circle")
snake.color("white")
snake.penup()
snake.shapesize(stretch_len=1.5,stretch_wid=1.5)
scoreboard=scoreboard()
screen.listen()
food=Food()
def move_up():
    snake.setheading(90)
def move_down():
    snake.setheading(270)
def move_left():
    snake.setheading(180)
def move_right():
    snake.setheading(0)
game_is_on=True
while game_is_on:
    snake.forward(20)
    time.sleep(0.1)
    screen.onkey(fun=move_up,key="Up")
    screen.onkey(fun=move_down,key="Down")
    screen.onkey(fun=move_left,key="Left")
    screen.onkey(fun=move_right,key="Right")

    if snake.distance(food)<15:
        food.refresh()
        scoreboard.increase_scoreboard()













screen.exitonclick()