from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fast")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_height = self.shapesize()[0] * 20  # Scale the height by 20 (default size)
        self.paddle_width = self.shapesize()[1] * 20   # Scale the width by 20 (default size)

        self.screen_height = screen_height // 2

    def set_starting_pos(self, x_cor):
        self.goto(x=x_cor, y=0)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y + self.paddle_height // 2 < self.screen_height:
            self.goto(self.xcor(), new_y)
        else: # Move paddle based on any remaining distance with the screen height
            y_cor = self.screen_height - self.paddle_height // 2
            self.goto(self.xcor(), y_cor)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y - self.paddle_height // 2 > -self.screen_height:
            self.goto(self.xcor(), new_y)
        else:
            y_cor = -self.screen_height + self.paddle_height // 2
            self.goto(self.xcor(), y_cor)
