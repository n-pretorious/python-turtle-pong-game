from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fast")
        self.shapesize(stretch_wid=3, stretch_len=0.5)

    def set_starting_pos(self, x_cor):
        self.goto(x=x_cor, y=0)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
