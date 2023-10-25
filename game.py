import pygame, sys, os, random, math
from pygame.locals import *
from obj.gobjects import *
from const import *
from style import *
from gmanager import GManager
from screens import GScreen, TitleScreen, GameScreen, OverScreen

pygame.init()
fps = pygame.time.Clock()
GAME_MANAGER = GManager()

# Screens
screen = TitleScreen()

# Canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32 )
pygame.display.set_caption('Asteroids')
    
def ss_handle_input():
    global screen
    for event in pygame.event.get():
        if event.type == KEYUP:
            GAME_MANAGER.playing_state = GManager.STATE_PLAYING
            screen = GameScreen()
            screen.reset_game()


def handle_input():
    global ship

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
    # draw(window)

    screen.draw(window)
    
    if GAME_MANAGER.playing_state == GManager.STATE_START:
        ss_handle_input()
    elif GAME_MANAGER.playing_state == GManager.STATE_PLAYING:
        # gscreen.draw(window)
        handle_input()
    elif GAME_MANAGER.playing_state == GManager.STATE_GAME_OVER:
        # oscreen.draw(window)
        ss_handle_input()
    
    screen.logic()

    update_screen()