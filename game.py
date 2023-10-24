import pygame, sys, os, random, math
from pygame.locals import *
from obj.gobjects import *
from const import *
from style import *
from gmanager import GManager
from screens import GameScreen

pygame.init()
fps = pygame.time.Clock()
GAME_MANAGER = GManager()

# Global
time = 0

# Globals for SHIP
gscreen = GameScreen()
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

label_title = title.render("ASTEROIDS", 1, GREEN)
label_press_key = write.render("Press any key", 1, GREEN)
label_game_over = title.render("GAME OVER", 1, RED)

def reset_game():
    global ship, asteroids
    gscreen.ship = Ship(WIDTH / 2 - 50, HEIGHT / 2 - 50, SHIP_SIZE, 0, ROTATION_SPEED)
    asteroids = []
    GAME_MANAGER.playing_state = GManager.STATE_PLAYING

def rot_center(image, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    
    return rot_image

def start_screen(canvas):
    canvas.blit(label_title, (WIDTH / 2 - label_title.get_width() / 2, HEIGHT / 2 - label_title.get_height() / 2))
    if GAME_MANAGER.time % 60 in range(0, 40):
        canvas.blit(label_press_key, (WIDTH / 2 - label_press_key.get_width() / 2, HEIGHT / 2 - label_press_key.get_height() / 2 + label_title.get_height() / 2))

def playing_screen(canvas):
    for i in range(0, len(asteroids)):
        canvas.blit(rot_center(planet, asteroids[i].angle), ( asteroids[i].x, asteroids[i].y))

    for i in range(0, len(gscreen.ship.bullets)):
        canvas.blit(rot_center(fire, gscreen.ship.bullets[i].angle), ( gscreen.ship.bullets[i].x, gscreen.ship.bullets[i].y))

    canvas.blit(rot_center(ship_sprite, gscreen.ship.angle), (gscreen.ship.x, gscreen.ship.y))
    canvas.blit(write.render("SCORE: {:n}".format(GAME_MANAGER.score), 1, GREEN), (0,0))

def game_over_screen(canvas):
    canvas.blit(label_game_over, (WIDTH / 2 - label_game_over.get_width() / 2, HEIGHT / 2 - label_game_over.get_height() / 2))

def draw(canvas):
    canvas.fill(BLACK)
    # canvas.blit(bg, (0, 0))
    # canvas.blit(debris, (time*.3,0))
    # canvas.blit(debris, (time*.3 - WIDTH,0))
    GAME_MANAGER.tiktak()

    if GAME_MANAGER.playing_state == GManager.STATE_START:
        start_screen(canvas)
    elif GAME_MANAGER.playing_state == GManager.STATE_PLAYING:
        playing_screen(canvas)
    elif GAME_MANAGER.playing_state == GManager.STATE_GAME_OVER:
        game_over_screen(canvas)
    

def ss_handle_input():
    for event in pygame.event.get():
        if event.type == KEYUP:
            reset_game()


def handle_input():
    global ship

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            gscreen.handle_input(event)


        # elif event.type == KEYDOWN:
        #     if event.key == K_LEFT:
        #         ship.rotating = True
        #         ship.direction = Ship.LEFT
        #     elif event.key == K_RIGHT:
        #         ship.rotating = True
        #         ship.direction = Ship.RIGHT
        #     elif event.key == K_UP:
        #         ship.moving = True
        #         ship.speed = START_SHIP_SPEED
        #     elif event.key == K_SPACE:
        #         ship.shooting = True

        # elif event.type == KEYUP:
        #     if event.key == K_LEFT or event.key == K_RIGHT:
        #         ship.rotating = False
        #     elif event.key == K_UP:
        #         ship.moving = False
        #     elif event.key == K_SPACE:
        #         ship.shooting = False

def controll_ship():
    gscreen.ship.rotate()
    gscreen.ship.move()
    gscreen.ship.shoot(BULLET_SPEED)

    for i in range(0, len(gscreen.ship.bullets)):
        gscreen.ship.bullets[i].move()


def is_collision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    
    return distance < DISTANCE_COLLISION

def create_asteroid():
    asteroid = Asteroid(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(0, 365), asteroid_speed)
    asteroids.append(asteroid)

def controll_asteroids():
    if GAME_MANAGER.time % time_create_asteroid == 0 and GAME_MANAGER.time > 0 and len(asteroids) < GAME_MANAGER.max_asteroids:
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

        if is_collision(asteroids[i].x, asteroids[i].y, gscreen.ship.x, gscreen.ship.y):
            GAME_MANAGER.playing_state = GManager.STATE_GAME_OVER

def game_logic():
    controll_ship()
    controll_asteroids()

def update_screen():
    pygame.display.update()
    fps.tick(60)

# Asteroids game loop
while True:
    draw(window)

    if GAME_MANAGER.playing_state == GManager.STATE_START:
        ss_handle_input()
    elif GAME_MANAGER.playing_state == GManager.STATE_PLAYING:
        handle_input()
        game_logic()
    elif GAME_MANAGER.playing_state == GManager.STATE_GAME_OVER:
        ss_handle_input()

    update_screen()