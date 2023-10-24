import pygame, os
from style import *
pygame.init()
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