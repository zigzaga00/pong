from paddle import Paddle
from turtle import Screen, Turtle

# set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()

screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")

screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")

game_on = True
while game_on:
    screen.update()



screen.exitonclick()