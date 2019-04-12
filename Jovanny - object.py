class Ball(object):
    def __init__(self):
        self.bounce = 10
        self.roll = 8
        self.throw = 4
        self.kick = 1
        self.pop = True

    def bounce(self):
        self.bounce += 0
        if self.bounce > 10:
            self.bounce = 10

    def roll(self):
        self.roll += 0
        if self.roll > 8:
            self.roll = 8

    def throw(self):
        self.throw += 0
        if self.throw > 4:
            self.throw = 4

    def kick(self):
        self.kick += 0
        if self.kick > 1:
            self.kick = 1

    def pop(self):
        self.pop += 0
        if self.pop > 0:
            self.pop = 0


my_ball = Ball

my_ball.bounce = 10
my_ball.roll = 8
my_ball.throw = 4
my_ball.kick = 1
my_ball.pop = 0
