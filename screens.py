import pygame
from pygame.locals import *
from abc import ABC, abstractclassmethod
from obj.gobjects import Ship
from const import START_SHIP_SPEED

class GScreen:
    @abstractclassmethod
    def handle_input():
        pass

    @abstractclassmethod
    def logic():
        pass

class GameScreen(GScreen):

    def __init__(self) -> None:
        super().__init__()
        self.ship = Ship()

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