from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for body in range(0, 3):
            self.add_body_to_snake((0 - body * 20, 0))

    def add_body_to_snake(self,position):
        new_snake = Turtle(shape='square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.goto(position)
        self.snake_body.append(new_snake)

    def reset_snake(self):
        for snakes in self.snake_body:
            snakes.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()

    def extend(self):
        # x = self.snake_body[-1].xcor()
        # y = self.snake_body[-1].ycor()
        # new_snake = Turtle(shape='square')
        # new_snake.color('white')
        # new_snake.penup()
        # new_snake.goto(self.snake_body[-1].position())
        # self.snake_body.append(new_snake)
        self.add_body_to_snake(self.snake_body[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_num - 1].xcor()
            new_y = self.snake_body[snake_num - 1].ycor()
            self.snake_body[snake_num].goto(x=new_x, y=new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].seth(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].seth(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].seth(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].seth(RIGHT)


