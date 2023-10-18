import pygame, sys, os, random, math
from pygame.locals import *
from gasteroid import GAsteroid
# from gclases import Asteroid
# gclases.
# Asteroid(1,2,4,5)
pygame.init()
fps = pygame.time.Clock()

#Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Globals
WIDTH = 800
HEIGHT = 600
current_speed = 7
time = 0
# Globals for SHIP
ship_x = WIDTH / 2 - 50
ship_y = HEIGHT / 2 - 50
ship_angle = 0
ship_rotation_speed = 7
ship_rotaiting = False
ship_speed = 0
ship_moving = False
ship_direction = -1
# Globals for ASTEROIDs
asteroids = []
asteroid_speed = 2

# Canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32 )
pygame.display.set_caption('Asteroids')

# Load images
# bg = pygame.image.load(os.path.join('images', 'bg.jpg'))
# debris = pygame.image.load(os.path.join('images', 'debris2_brown.png'))
ship = pygame.image.load(os.path.join('assets', 'img', 'sun.png'))
planet = pygame.image.load(os.path.join('assets', 'img', 'planet.png'))

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    
    return rot_image

def draw(canvas):
    global time
    canvas.fill(BLACK)
    # canvas.blit(bg, (0, 0))
    # canvas.blit(debris, (time*.3,0))
    # canvas.blit(debris, (time*.3 - WIDTH,0))
    time = time + 1
    
    for i in range(0, len(asteroids)):
        canvas.blit(rot_center(planet, asteroids[i].angle), ( asteroids[i].x, asteroids[i].y))

    canvas.blit(rot_center(ship, ship_angle), ( ship_x, ship_y))
    

def handle_input():
    global ship_angle, ship_rotaiting, ship_direction, ship_moving, ship_speed

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                ship_rotaiting = True
                ship_direction = 1
            elif event.key == K_RIGHT:
                ship_rotaiting = True
                ship_direction = -1
            elif event.key == K_UP:
                ship_moving = True
                ship_speed = current_speed

        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                ship_rotaiting = False
            elif event.key == K_UP:
                ship_moving = False

def move_ship():
    global ship_angle, ship_x, ship_y, ship_speed
    
    if (ship_rotaiting):
        ship_angle = ship_angle + ship_direction * ship_rotation_speed
    if (ship_moving or ship_speed > 0):
        ship_x = (ship_x + math.cos(math.radians(ship_angle)) * ship_speed)
        ship_y = (ship_y - math.sin(math.radians(ship_angle)) * ship_speed)
        if ship_moving == False:
            ship_speed = ship_speed - .1

def create_asteroid():
    # pass
    if time % 10 == 0 and time > 0:
        ast = GAsteroid(random(0, WIDTH), random(0, HEIGHT), random(0, 365), asteroid_speed)
        asteroids.append(ast)

def move_asteroids():
    for i in range(0, len(asteroids)):
        asteroids[i].x = (asteroids[i].x + math.cos(math.radians(asteroids[i].angle)) * asteroids[i].speed)
        asteroids[i].y = (asteroids[i].y - math.sin(math.radians(asteroids[i].angle)) * asteroids[i].speed)

def game_logic():
    move_ship()
    create_asteroid()
    move_asteroids()

def update_screen():
    pygame.display.update()
    fps.tick(60)

# Asteroids game loop
while True:
    draw(window)
    handle_input()
    game_logic()
    update_screen()