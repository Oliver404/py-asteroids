import pygame, sys, os, random, math
from pygame.locals import *
from gobjects import *

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
DISTANCE_COLLISION = 27
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
time_create_asteroid = 21

# Canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32 )
pygame.display.set_caption('Asteroids')

# Load images
# bg = pygame.image.load(os.path.join('images', 'bg.jpg'))
# debris = pygame.image.load(os.path.join('images', 'debris2_brown.png'))
ship = pygame.image.load(os.path.join('assets', 'img', 'sun.png'))
planet = pygame.image.load(os.path.join('assets', 'img', 'planet.png'))
star = pygame.image.load(os.path.join('assets', 'img', 'star.png'))

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

def is_collision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    
    return distance < DISTANCE_COLLISION

def create_asteroid():
    if time % time_create_asteroid == 0 and time > 0:
        asteroid = Asteroid(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(0, 365), asteroid_speed)
        asteroids.append(asteroid)

def controll_asteroids():
    create_asteroid()

    for i in range(0, len(asteroids)):
        asteroids[i].move()

        if (asteroids[i].y > HEIGHT + 100):
            asteroids[i].y = 0
        elif (asteroids[i].y < 0 - 100):
            asteroids[i].y = HEIGHT

        if (asteroids[i].x > WIDTH + 100):
            asteroids[i].x = 0
        elif (asteroids[i].x < 0 - 100):
            asteroids[i].x = WIDTH

        if is_collision(asteroids[i].x, asteroids[i].y, ship_x, ship_y):
            print("GAME OVER")
            # exit()

def game_logic():
    move_ship()
    controll_asteroids()

def update_screen():
    pygame.display.update()
    fps.tick(60)


# Asteroids game loop
while True:
    draw(window)
    handle_input()
    game_logic()
    update_screen()