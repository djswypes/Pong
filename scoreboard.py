from turtle import Turtle

FONT = ('Courier', 60, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto((-100, 200))
        self.write(f"{self.l_score}", align='center', font=FONT)
        self.goto((100, 200))
        self.write(f"{self.r_score}", align='center', font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
