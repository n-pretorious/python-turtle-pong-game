from paddle import Paddle


class Team:
    def __init__(self, screen_width):
        self.score = 0
        self.side = None
        self.paddle = Paddle(screen_width)

    def move_paddle_up(self):
        self.paddle.move_up()

    def move_paddle_down(self):
        self.paddle.move_down()

    def set_starting_pos(self, x_cor):
        self.paddle.set_starting_pos(x_cor)
