from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from time import sleep
from turtle import Screen, Turtle

# set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# set up the scoreboard
scoreboard = Scoreboard()

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
    sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()
    # check for collision with top or bottom walls
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.bounce_y()
    # check for collisions with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # check for r_paddle or l_paddle miss
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()
screen.exitonclick()
