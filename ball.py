from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.x_move = 5
        self.y_move = 5
        self.penup()

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
