from ball import Ball
from paddle import Paddle
from time import sleep
from turtle import Screen, Turtle

# set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")

screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")

game_on = True
while game_on:
    sleep(0.025)
    ball.move_ball()
    screen.update()
    # check for collision with top or bottom walls
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.bounce_y()
    # check for collisions with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()
