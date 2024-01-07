from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from score_board import Board
import sys


def play():
    screen = Screen()
    screen.setup(width=590, height=590)
    screen.bgcolor("black")
    screen.title("Snake")

    screen.tracer(0)

    snake = Snake()
    food = Food()
    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    board = Board()
    game_is_on = True

    while game_is_on:
        screen.update()
        if snake.head.distance(food.s) < 15:
            food.goto()
            snake.extend_snake()
            board.add()
        if snake.head.pos()[0] > 282 or snake.head.pos()[0] < -282 or snake.head.pos()[1] > \
                282 or snake.head.pos()[1] < -282 or snake.self_crush():
            board.game_over()

            def again():
                offer = screen.textinput("Play again", "Type Y to play again or press cancel")
                if offer == "y":
                    screen.clear()
                    return play()
                else:
                    sys.exit()

            again()
            game_is_on = False

        sleep(0.1)
        snake.move()

    screen.exitonclick()


play()
