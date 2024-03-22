from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.ball_speed = 0.025
        self.x_move = 2.5
        self.y_move = 2.5
        self.penup()

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def reset_pos(self):
        self.goto(0, 0)
        self.ball_speed = 0.025
        self.bounce_x()    
