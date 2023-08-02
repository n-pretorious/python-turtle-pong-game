from paddle import Paddle
from score import ScoreBoard


class Team:
    def __init__(self, screen_width, screen_height, x_score_position):
        self.score = 0
        self.side = None
        self.paddle = Paddle(screen_height)
        self.score = ScoreBoard(x_score_position, screen_height)

    def move_paddle_up(self):
        self.paddle.move_up()

    def move_paddle_down(self):
        self.paddle.move_down()

    def set_starting_pos(self, x_cor):
        self.paddle.set_starting_pos(x_cor)
