import pygame, sys, os, random, math
from pygame.locals import *
from obj.gobjects import *
from const import *
from style import *
from gmanager import GManager
from screens import GScreen, TitleScreen, GameScreen, OverScreen

pygame.init()
fps = pygame.time.Clock()



# Canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32 )
pygame.display.set_caption('Asteroids')

def on_state_change():
    global screen

    if GAME_MANAGER.playing_state == GManager.STATE_START:
        screen = TitleScreen(GAME_MANAGER)
    elif GAME_MANAGER.playing_state == GManager.STATE_PLAYING:
        screen = GameScreen(GAME_MANAGER)
        screen.reset_game()
    elif GAME_MANAGER.playing_state == GManager.STATE_GAME_OVER:
        screen = OverScreen(GAME_MANAGER)

GAME_MANAGER = GManager(on_state_change)
# Screens
screen = TitleScreen(GAME_MANAGER)

def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            screen.handle_input(event)

def update_screen():
    pygame.display.update()
    fps.tick(60)

# Asteroids game loop
while True:
    screen.draw(window)
    handle_input()
    screen.logic()
    update_screen()