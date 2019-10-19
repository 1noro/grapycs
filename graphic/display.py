#graphic.displays
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .color import stdCs

### FUNCTIONS ##################################################################
def displaygame(screen):
    # Set the screen background
    screen.fill(colorbg)

    map.draw(screen)
    map.goal.draw(screen)
    if not victory:
        map.player.draw(screen)
    else:
        print_result(screen, stdsize, width, height, lvl_time, color1, color2, txt, font_file)
