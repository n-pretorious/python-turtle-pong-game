from turtle import Screen, Turtle
from team import Team

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
LEFT_TEAM_STARTING_POSITION = -SCREEN_WIDTH // 2 + 10
RIGHT_TEAM_STARTING_POSITION = SCREEN_WIDTH // 2 - 10


class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")
        self.welcome_message = self.create_turtle()

        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.team_1 = Team(SCREEN_HEIGHT)
        self.team_1.paddle.set_starting_pos(LEFT_TEAM_STARTING_POSITION)

        self.team_2 = Team(SCREEN_HEIGHT)
        self.team_2.paddle.set_starting_pos(RIGHT_TEAM_STARTING_POSITION)

        self.bind_keys()

    def show_start_message(self):
        self.welcome_message.color("white")
        self.welcome_message.write("Press 'space' key to start", align="center", font=("Arial", 18, "normal"))

    def bind_keys(self):
        self.screen.listen()

        self.screen.onkey(fun=self.team_1.paddle.move_up, key="w")
        self.screen.onkey(fun=self.team_1.paddle.move_down, key="s")
        self.screen.onkey(fun=self.team_2.paddle.move_up, key="Up")
        self.screen.onkey(fun=self.team_2.paddle.move_down, key="Down")
        self.screen.onkey(fun=self.start, key="space")

    def start(self):
        self.show_start_message()
        self.welcome_message.clear()

    @staticmethod
    def create_turtle():
        turtle = Turtle()
        turtle.penup()
        turtle.hideturtle()
        return turtle


if __name__ == "__main__":
    pong_game = PongGame()
    # pong_game.start()
    pong_game.screen.mainloop()

