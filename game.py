import pygame, sys, os, random, math
from pygame.locals import *
from gobjects import *
from const import *
from gmanager import GManager

pygame.init()
fps = pygame.time.Clock()
GAME_MANAGER = GManager()

#Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Globals
score = 0
current_speed = 7
time = 0

# Globals for SHIP
ship = Ship(WIDTH / 2 - 50, HEIGHT / 2 - 50, SHIP_SIZE, 0, ROTATION_SPEED)

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
ship_sprite = pygame.image.load(os.path.join('assets', 'img', 'sun.png'))
planet = pygame.image.load(os.path.join('assets', 'img', 'planet.png'))
star = pygame.image.load(os.path.join('assets', 'img', 'star.png'))
fire = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'img', 'fire.png')), (10, 10))

title = pygame.font.SysFont('Consolas', 96, True)
write = pygame.font.SysFont('Consolas', 24, True)

label_title = title.render("ASTEROIDS".format(score), 1, GREEN)

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    
    return rot_image

def start_screen(canvas):
    canvas.blit(label_title, (WIDTH / 2 - label_title.get_width() / 2, HEIGHT / 2 - label_title.get_height() / 2))

def playing_screen(canvas):
    for i in range(0, len(asteroids)):
        canvas.blit(rot_center(planet, asteroids[i].angle), ( asteroids[i].x, asteroids[i].y))

    for i in range(0, len(ship.bullets)):
        canvas.blit(rot_center(fire, ship.bullets[i].angle), ( ship.bullets[i].x, ship.bullets[i].y))

    canvas.blit(rot_center(ship_sprite, ship.angle), (ship.x, ship.y))
    canvas.blit(write.render("SCORE: {:n}".format(score), 1, GREEN), (0,0))

def draw(canvas):
    global time
    canvas.fill(BLACK)
    # canvas.blit(bg, (0, 0))
    # canvas.blit(debris, (time*.3,0))
    # canvas.blit(debris, (time*.3 - WIDTH,0))
    time = time + 1

    print(GAME_MANAGER.playing_state)

    if GAME_MANAGER.playing_state == GManager.STATE_START:
        start_screen(canvas)
    elif GAME_MANAGER.playing_state == GManager.STATE_PLAYING:
        playing_screen(canvas)
    

def handle_input():
    global ship

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                ship.rotating = True
                ship.direction = Ship.LEFT
            elif event.key == K_RIGHT:
                ship.rotating = True
                ship.direction = Ship.RIGHT
            elif event.key == K_UP:
                ship.moving = True
                ship.speed = current_speed
            elif event.key == K_SPACE:
                ship.shooting = True
            elif event.key == K_DELETE:
                GAME_MANAGER.playing_state = GManager.STATE_PLAYING

        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                ship.rotating = False
            elif event.key == K_UP:
                ship.moving = False
            elif event.key == K_SPACE:
                ship.shooting = False

def controll_ship():
    ship.rotate()
    ship.move()
    ship.shoot(BULLET_SPEED)

    for i in range(0, len(ship.bullets)):
        ship.bullets[i].move()


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

        if is_collision(asteroids[i].x, asteroids[i].y, ship.x, ship.y):
            GAME_MANAGER.playing_state = GManager.STATE_GAME_OVER
            # exit()

def game_logic():
    controll_ship()
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