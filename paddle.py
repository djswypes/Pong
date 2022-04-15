from turtle import Turtle

DOWN = 270
UP = 90


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape('square')
        self.shapesize(5, 1)
        self.penup()
        self.color('white')
        self.goto(coordinate)

    def move(self, direction):
        new_y = self.ycor() + direction
        self.goto(self.xcor(), new_y)

    def up(self):
        self.move(20)

    def down(self):
        self.move(-20)
