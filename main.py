from turtle import Screen

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


class PongGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.title("Pong Game")

        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    def start(self):
        self.screen.exitonclick()


if __name__ == "__main__":
    pong_game = PongGame()
    pong_game.start()
