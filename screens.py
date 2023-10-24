import pygame, random
from pygame.locals import *
from abc import ABC, abstractclassmethod
from obj.gobjects import Ship, Asteroid
from const import *
from g_utils import is_collision, rot_center
from assets import *
class GScreen:
    def __init__(self) -> None:
        self. time = 0

    @abstractclassmethod
    def handle_input(self, event):
        pass

    def logic(self):
        self.time += 1

    @abstractclassmethod
    def draw(self, canvas):
        pass

class TitleScreen(GScreen):
    
    def handle_input(self, event):
        if event.type == KEYUP:
            pass

    def logic(self):
        super().login()
        print("Title Screen Logic")

    def draw(self, canvas):
        canvas.blit(label_title, (WIDTH / 2 - label_title.get_width() / 2, HEIGHT / 2 - label_title.get_height() / 2))
        if self.time % 60 in range(0, 40):
            canvas.blit(label_press_key, (WIDTH / 2 - label_press_key.get_width() / 2, HEIGHT / 2 - label_press_key.get_height() / 2 + label_title.get_height() / 2))

class OverScreen(GScreen):
    
    def handle_input(self, event):
        if event.type == KEYUP:
            pass

    def logic(self):
        super().login()
        print("Over Screen Logic")

    def draw(self, canvas):
        canvas.blit(label_game_over, (WIDTH / 2 - label_game_over.get_width() / 2, HEIGHT / 2 - label_game_over.get_height() / 2))

class GameScreen(GScreen):
    # TODO: Move this to correct way
    max_asteroids = 10
    time_create_asteroid = 21
    asteroid_speed = 2

    def __init__(self) -> None:
        super().__init__()
        self.ship = Ship()
        self.asteroids = []
        self.score = 0

    def handle_input(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.ship.rotating = True
                self.ship.direction = Ship.LEFT
            elif event.key == K_RIGHT:
                self.ship.rotating = True
                self.ship.direction = Ship.RIGHT
            elif event.key == K_UP:
                self.ship.moving = True
                self.ship.speed = START_SHIP_SPEED
            elif event.key == K_SPACE:
                self.ship.shooting = True

        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                self.ship.rotating = False
            elif event.key == K_UP:
                self.ship.moving = False
            elif event.key == K_SPACE:
                self.ship.shooting = False


    def logic(self):
        self.time += 1
        self.controll_ship()
        self.controll_asteroids()

    def draw(self, canvas):
        for i in range(0, len(self.asteroids)):
            canvas.blit(rot_center(planet, self.asteroids[i].angle), ( self.asteroids[i].x, self.asteroids[i].y))

        for i in range(0, len(self.ship.bullets)):
            canvas.blit(rot_center(fire, self.ship.bullets[i].angle), ( self.ship.bullets[i].x, self.ship.bullets[i].y))

        canvas.blit(rot_center(ship_sprite, self.ship.angle), (self.ship.x, self.ship.y))
        canvas.blit(write.render("SCORE: {:n}".format(self.score), 1, GREEN), (0,0))

    def reset_game(self):
        global ship, asteroids
        self.ship = Ship(WIDTH / 2 - 50, HEIGHT / 2 - 50, SHIP_SIZE, 0, ROTATION_SPEED)
        self.asteroids = []
        # TODO: Mandar evento de que ahora se esta jugando
        # GAME_MANAGER.playing_state = GManager.STATE_PLAYING

    def create_asteroid(self):
        asteroid = Asteroid(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(0, 365), GameScreen.asteroid_speed)
        self.asteroids.append(asteroid)

    def controll_ship(self):
        self.ship.rotate()
        self.ship.move()
        self.ship.shoot(BULLET_SPEED)

        for i in range(0, len(self.ship.bullets)):
            self.ship.bullets[i].move()

    def controll_asteroids(self):
        if self.time % GameScreen.time_create_asteroid == 0 and self.time > 0 and len(self.asteroids) < GameScreen.max_asteroids:
            self.create_asteroid()

        for i in range(0, len(self.asteroids)):
            self.asteroids[i].move()

            if (self.asteroids[i].y > HEIGHT + 100):
                self.asteroids[i].y = 0
            elif (self.asteroids[i].y < 0 - 100):
                self.asteroids[i].y = HEIGHT

            if (self.asteroids[i].x > WIDTH + 100):
                self.asteroids[i].x = 0
            elif (self.asteroids[i].x < 0 - 100):
                self.asteroids[i].x = WIDTH

            if is_collision(self.asteroids[i].x, self.asteroids[i].y, self.ship.x, self.ship.y, DISTANCE_COLLISION):
                # TODO: Delete print and add login  
                # GAME_MANAGER.playing_state = GManager.STATE_GAME_OVER
                print("GameOver")