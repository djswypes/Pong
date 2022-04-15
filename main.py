from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.tracer(0)
screen.title('Pong')
l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = ScoreBoard()
screen.listen()
screen.onkeypress(key='Up', fun=r_paddle.up)
screen.onkeypress(key='Down', fun=r_paddle.down)
screen.onkeypress(key='w', fun=l_paddle.up)
screen.onkeypress(key='s', fun=l_paddle.down)
game_is_on = True

while game_is_on:
    ball.move()
    time.sleep(ball.speed)
    screen.update()

    if r_paddle.ycor() > 260:
        r_paddle.goto((380, 260))

    if r_paddle.ycor() < -220:
        r_paddle.goto((380, -240))

    if l_paddle.ycor() > 260:
        l_paddle.goto((-380, 260))

    if l_paddle.ycor() < -220:
        l_paddle.goto((-380, -240))

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.x_bounce()

    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset()

    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()
