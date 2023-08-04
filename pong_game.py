from turtle import Turtle
from team import Team
from ball import Ball
import time


def ball_matches_paddle(ball_y, paddle):
    top_y = paddle.ycor() + paddle.paddle_height / 2
    bottom_y = paddle.ycor() - paddle.paddle_height / 2
    return bottom_y <= ball_y <= top_y


class PongGame:
    def __init__(self, screen, screen_width, screen_height, winning_score):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.winning_score = winning_score
        self.welcome_message = self.create_turtle()
        self.screen.tracer(0)

        self.l_team = Team(screen_width=screen_width, screen_height=screen_height, x_score_position=-30)
        self.l_team.paddle.set_starting_pos(-self.screen_width // 2 + 10)
        self.r_team = Team(screen_width=screen_width, screen_height=screen_height, x_score_position=30)
        self.r_team.paddle.set_starting_pos(self.screen_width // 2 - 10)
        self.ball = Ball()
        self.ball.set_middle()
        self.ball.set_initial_direction()  # Set an initial direction for the ball
        self.bind_keys()

    def show_start_message(self):
        self.welcome_message.color("white")
        self.welcome_message.write("Press 'space' key to start", align="center", font=("Arial", 18, "normal"))

    def bind_keys(self):
        self.screen.listen()
        self.screen.onkeypress(fun=self.l_team.move_paddle_up, key="w")
        self.screen.onkeypress(fun=self.l_team.move_paddle_down, key="s")
        self.screen.onkeypress(fun=self.r_team.move_paddle_up, key="Up")
        self.screen.onkeypress(fun=self.r_team.move_paddle_down, key="Down")
        self.screen.onkey(fun=self.setup_game, key="space")

    def detect_collision_with_wall(self):
        if self.ball.ycor() + self.ball.radius >= self.screen_height // 2 or self.ball.ycor() - self.ball.radius \
                <= -self.screen_height // 2:
            self.ball.bounce_y()

    def detect_collision_with_paddle(self):
        if self.ball.dx > 0 and ball_matches_paddle(self.ball.ycor(), self.r_team.paddle):
            if self.ball.xcor() + self.ball.radius >= self.r_team.paddle.xcor() - self.r_team.paddle.paddle_width / 2:
                self.ball.bounce_x()
        elif self.ball.dx < 0 and ball_matches_paddle(self.ball.ycor(), self.l_team.paddle):
            if self.ball.xcor() - self.ball.radius <= self.l_team.paddle.xcor() + self.l_team.paddle.paddle_width / 2:
                self.ball.bounce_x()

    def setup_game(self):
        self.welcome_message.clear()
        self.l_team.score.update_score_display()
        self.r_team.score.update_score_display()
        self.ball.move_random_direction()

        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(self.ball.ball_speed)
            self.ball.move()
            self.detect_collision_with_wall()
            self.detect_collision_with_paddle()

            if self.ball.xcor() < int(-self.screen_width // 2):
                self.r_team.score.increase(1)
                if self.r_team.score.get_score() >= self.winning_score:
                    self.game_over(winner="Right Team")
                    game_is_on = False
                else:
                    self.ball.set_middle()
                    self.ball.set_initial_direction()
                    self.ball.move_random_direction()
            elif self.ball.xcor() > int(self.screen_width // 2):
                self.l_team.score.increase(1)
                if self.l_team.score.get_score() >= self.winning_score:
                    self.game_over(winner="Left Team")
                    game_is_on = False
                else:
                    self.ball.set_middle()
                    self.ball.set_initial_direction()  # Reset the ball's direction
                    self.ball.move_random_direction()

    def game_over(self, winner):
        self.welcome_message.write(f"Game Over! {winner} wins!", align="center", font=("Arial", 18, "normal"))

    @staticmethod
    def create_turtle():
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        return turtle
