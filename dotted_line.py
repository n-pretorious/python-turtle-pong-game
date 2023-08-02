from turtle import Turtle


class DottedLine(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.screen_height = screen_height
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -screen_height // 2)
        self.setheading(90)
        self.pendown()
        self.pensize(2)
        self.dotted_line()

    def dotted_line(self):
        for _ in range(self.screen_height // 20):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
