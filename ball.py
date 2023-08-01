from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def move_up_forward(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10

        self.goto(x=new_x, y=new_y)

    def move_up_back(self):
        new_x = self.xcor() - 10
        new_y = self.ycor() + 10

        self.goto(x=new_x, y=new_y)

    def move_down_forward(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10

        self.goto(x=new_x, y=new_y)

    def move_down_back(self):
        new_x = self.xcor() - 10
        new_y = self.ycor() - 10

        self.goto(x=new_x, y=new_y)
