import math

class Ship:
    LEFT = 1
    RIGHT = -1
    DEFAULT_DECELERATION = 1
    def __init__(self, x = 0, y = 0, size = 0, speed = 0, rotation_speed = 0, angle = 0, deceleration = DEFAULT_DECELERATION, direction = RIGHT, moving = False, rotating = False, shooting = False, bullets = []):
        self.x = x
        self.y = y
        self.speed = speed
        self.rotation_speed = rotation_speed
        self.angle = angle
        self.deceleration = deceleration
        self.direction = direction
        self.moving = False
        self.rotating = False
        self.shooting = shooting
        self.bullets = bullets

    def rotate(self):
        if self.rotating:
            self.angle += self.direction * self.rotation_speed

    def move(self):
        if self.moving or self.speed > 0:
            self.x = (self.x + math.cos(math.radians(self.angle)) * self.speed)
            self.y = (self.y - math.sin(math.radians(self.angle)) * self.speed)
            if not self.moving:
                self.speed = self.speed - self.deceleration
    
    def shoot(self, speed):
        if self.shooting:
            # TODO: Modificar los 45 para que no se usen por HARDCODEO
            self.bullets.append(Bullet(self.x + 45, self.y + 45, self.angle, speed))

class Asteroid:
    def __init__(self, x, y, angle, speed, size):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = speed
        self.size = size

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

    def move(self):
        self.x = (self.x + math.cos(math.radians(self.angle)) * self.speed)
        self.y = (self.y - math.sin(math.radians(self.angle)) * self.speed)