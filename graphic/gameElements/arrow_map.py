#graphic.gameElements.arrow_map
#by boot1110001

### IMPORTS ####################################################################
import pygame
from ..color import stdCs
from ..elements.sq_square import SQSquare

### CLASSES ####################################################################
class ArrowMap:
    def __init__(self, sqx, sqy, sqpx):
        self.sqpx = sqpx
        self.sqx = sqx
        self.sqy = sqy

    def draw(self, screen, pressed_keys):
        # up, left, down, right
        SQSquare(self.sqx+4, self.sqy, 4, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
        SQSquare(self.sqx, self.sqy+4, 4, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
        SQSquare(self.sqx+4, self.sqy+4, 4, self.sqpx, stdCs.STAR_CMD_BLUE).draw(screen)
        SQSquare(self.sqx+8, self.sqy+4, 4, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)

        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            SQSquare(self.sqx+4, self.sqy, 4, self.sqpx, stdCs.ROSE_RED).draw(screen)
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            SQSquare(self.sqx, self.sqy+4, 4, self.sqpx, stdCs.ROSE_RED).draw(screen)
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            SQSquare(self.sqx+4, self.sqy+4, 4, self.sqpx, stdCs.ROSE_RED).draw(screen)
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            SQSquare(self.sqx+8, self.sqy+4, 4, self.sqpx, stdCs.ROSE_RED).draw(screen)
