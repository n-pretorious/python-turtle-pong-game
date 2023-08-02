from turtle import Screen, Turtle
from team import Team
from dotted_line import DottedLine
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LEFT_TEAM_STARTING_POSITION = -SCREEN_WIDTH // 2 + 10
RIGHT_TEAM_STARTING_POSITION = SCREEN_WIDTH // 2 - 10
WINNING_SCORE = 10  # Adjust this value as needed


class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.welcome_message = self.create_turtle()

        self.screen.tracer(0)
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        self.l_team = Team(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT, x_score_position=-30)
        self.l_team.paddle.set_starting_pos(LEFT_TEAM_STARTING_POSITION)

        self.r_team = Team(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT, x_score_position=30)
        self.r_team.paddle.set_starting_pos(RIGHT_TEAM_STARTING_POSITION)

        self.ball = Ball()
        self.ball.set_middle()
        self.ball.set_initial_direction()  # Set an initial direction for the ball

        self.bind_keys()

    def show_start_message(self):
        self.welcome_message.color("white")
        self.welcome_message.write("Press 'space' key to start", align="center", font=("Arial", 18, "normal"))

    def bind_keys(self):
        self.screen.listen()

        self.screen.onkeypress(fun=self.l_team.paddle.move_up, key="w")
        self.screen.onkeypress(fun=self.l_team.paddle.move_down, key="s")
        self.screen.onkeypress(fun=self.r_team.paddle.move_up, key="Up")
        self.screen.onkeypress(fun=self.r_team.paddle.move_down, key="Down")
        self.screen.onkey(fun=self.setup_game, key="space")

    def detect_collision_with_wall(self):
        if (
                self.ball.ycor() + self.ball.radius >= SCREEN_HEIGHT // 2 or
                self.ball.ycor() - self.ball.radius <= -SCREEN_HEIGHT // 2
        ):
            self.ball.bounce_y()

    def detect_collision_with_paddle(self):
        ball_x = self.ball.xcor()
        ball_y = self.ball.ycor()
        ball_radius = self.ball.radius

        if self.ball.dx > 0 and ball_y in self.get_paddle_y_coordinates(self.r_team.paddle):
            if ball_x + ball_radius >= self.r_team.paddle.xcor() - self.r_team.paddle.paddle_width / 2:
                self.ball.bounce_x()
        elif self.ball.dx < 0 and ball_y in self.get_paddle_y_coordinates(self.l_team.paddle):
            if ball_x - ball_radius <= self.l_team.paddle.xcor() + self.l_team.paddle.paddle_width / 2:
                self.ball.bounce_x()

    @staticmethod
    def get_paddle_y_coordinates(paddle):
        top_y = paddle.ycor() + paddle.paddle_height / 2
        bottom_y = paddle.ycor() - paddle.paddle_height / 2

        y_coordinates = [y for y in range(int(bottom_y), int(top_y) + 1)]
        return y_coordinates

    def ball_matches_paddle(self, ball_y, paddle):
        paddle_y_coordinates = self.get_paddle_y_coordinates(paddle)
        return ball_y in paddle_y_coordinates

    def setup_game(self):
        self.welcome_message.clear()

        DottedLine(SCREEN_HEIGHT)
        self.l_team.score.update_score_display()
        self.r_team.score.update_score_display()

        self.ball.move_random_direction()
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.05)

            self.ball.move()
            self.detect_collision_with_wall()
            self.detect_collision_with_paddle()

            if self.ball.xcor() < int(-SCREEN_WIDTH // 2):
                self.r_team.score.increase(1)
                if self.r_team.score.get_score() >= WINNING_SCORE:
                    self.game_over(winner="Right Team")
                    game_is_on = False
                else:
                    self.ball.set_middle()
                    self.ball.set_initial_direction()
                    self.ball.move_random_direction()

            elif self.ball.xcor() > int(SCREEN_WIDTH // 2):
                self.l_team.score.increase(1)
                if self.l_team.score.get_score() >= WINNING_SCORE:
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


if __name__ == "__main__":
    pong_game = PongGame()
    pong_game.show_start_message()
    pong_game.screen.mainloop()
