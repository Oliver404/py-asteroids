import math

class Ship:
    def __init__(self, x, y, speed = 0, angle = 0, shooting = False):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.shooting = shooting

class Asteroid:
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed

    def move(self):
        self.x = (self.x + math.cos(math.radians(self.angle)) * self.speed)
        self.y = (self.y - math.sin(math.radians(self.angle)) * self.speed)

class Bullet:
    def __init__(self, x, y, angle, speed):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        # self.power = power