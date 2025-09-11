from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].ycor() < - 280:
        # game_is_on = False
        # score_board.game_over()
        score_board.reset_scoreboard()
        snake.reset_snake()

    for snake_part in snake.snake_body[1:]:
        if snake.snake_body[0].distance(snake_part) < 10:
            # game_is_on = False
            # score_board.game_over()
            score_board.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()
