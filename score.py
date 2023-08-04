from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, x_cor, screen_height):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self._x_cor = x_cor
        self._y_cor = screen_height / 2 - 100
        self.goto(x=x_cor, y=self._y_cor)
        self.color("white")

    def get_score(self):
        return self.score

    def increase(self, points):
        self.score += points
        self.update_score_display()

    def update_score_display(self):
        self.clear()
        self.penup()
        self.goto(x=self._x_cor, y=self._y_cor)
        self.write(f"{self.score}", align="center", font=("Courier", 50, "normal"))
