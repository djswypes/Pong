from turtle import Turtle

MOVEMENT = [10, 10]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.goto((0, 0))
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + MOVEMENT[0]
        new_y = self.ycor() + MOVEMENT[1]
        self.goto((new_x, new_y))

    def reset(self):
        self.goto((0, 0))
        self.x_bounce()
        self.speed = 0.1

    @staticmethod
    def y_bounce():
        MOVEMENT[1] *= -1

    def x_bounce(self):
        MOVEMENT[0] *= -1
        self.speed *= 0.9
