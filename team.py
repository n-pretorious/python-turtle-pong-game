from paddle import Paddle

class Team:
    def __init__(self):
        self.score = 0
        self.paddle = Paddle()

    def move_paddle_up(self):
        self.paddle.move_up()

    def move_paddle_down(self):
        self.paddle.move_down()

    def set_starting_pos(self, x_cor):
        self.paddle.set_starting_pos(x_cor)
