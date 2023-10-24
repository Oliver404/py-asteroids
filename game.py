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
tscreen = TitleScreen()
gscreen = GameScreen()
oscreen = OverScreen()

# Canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32 )
pygame.display.set_caption('Asteroids')


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
            GAME_MANAGER.playing_state = GManager.STATE_PLAYING
            gscreen.reset_game()


def handle_input():
    global ship

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            gscreen.handle_input(event)

def update_screen():
    pygame.display.update()
    fps.tick(60)

# Asteroids game loop
while True:
    # draw(window)

    if GAME_MANAGER.playing_state == GManager.STATE_START:
        tscreen.draw(window)
        ss_handle_input()
    elif GAME_MANAGER.playing_state == GManager.STATE_PLAYING:
        gscreen.draw(window)
        handle_input()
        gscreen.logic()
    elif GAME_MANAGER.playing_state == GManager.STATE_GAME_OVER:
        oscreen.draw(window)
        ss_handle_input()

    update_screen()