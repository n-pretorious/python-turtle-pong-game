from turtle import Screen
from pong_game import PongGame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WINNING_SCORE = 3

if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    pong_game = PongGame(screen, SCREEN_WIDTH, SCREEN_HEIGHT, WINNING_SCORE)
    pong_game.show_start_message()
    screen.mainloop()
