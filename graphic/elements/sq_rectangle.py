#graphic.elements.rectangle
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .rectangle import Rectangle

### CLASSES ####################################################################
class SQRectangle(Rectangle):
    def __init__(self, sqx, sqy, sqWidth, sqHeight, sqpx, color):
        self.x=sqx * sqpx
        self.y=sqy * sqpx
        self.width=sqWidth * sqpx
        self.height=sqHeight * sqpx
        self.color=color

        self.sqpx=sqpx
        self.sqx=sqx
        self.sqy=sqy
        self.sqWidth=sqWidth
        self.sqHeight=sqHeight
