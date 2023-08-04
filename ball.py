from turtle import Turtle
import random

MOVE_SPEED = 6
BALL_RADIUS = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.dy = None
        self.dx = None
        self.shape("circle")
        self.color("white")
        self.penup()
        self.radius = BALL_RADIUS
        self.set_initial_direction()
        self.ball_speed = 0.05

    def set_middle(self):
        self.goto(0, 0)
        self.ball_speed = 0.05

    def set_initial_direction(self):
        self.dx = random.choice([-1, 1]) * MOVE_SPEED
        self.dy = random.choice([-1, 1]) * MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.ball_speed *= 0.9

    def move_up_forward(self):
        self.dx = MOVE_SPEED
        self.dy = MOVE_SPEED

    def move_up_back(self):
        self.dx = -MOVE_SPEED
        self.dy = MOVE_SPEED

    def move_down_forward(self):
        self.dx = MOVE_SPEED
        self.dy = -MOVE_SPEED

    def move_down_back(self):
        self.dx = -MOVE_SPEED
        self.dy = -MOVE_SPEED

    def move_random_direction(self):
        self.dx = random.choice([-1, 1]) * MOVE_SPEED
        self.dy = random.choice([-1, 1]) * MOVE_SPEED
