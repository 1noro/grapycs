#graphic.elements.square
#by boot1110001

### IMPORTS ####################################################################
import pygame
from .rectangle import Rectangle

### CLASSES ####################################################################
class SQSquare(Rectangle):
    def __init__(self, sqx, sqy, sqWidth, sqpx, color):
        self.x=sqx * sqpx
        self.y=sqy * sqpx
        self.width=sqWidth * sqpx
        self.height=sqWidth * sqpx
        self.color=color
        self.sqx=sqx
        self.sqy=sqy
        self.sqpx=sqpx

    # def set_sqpx(self, new_sqpx):
    #     self.width=new_sqpx
    #     self.height=new_sqpx
    #     self.sqpx=new_sqpx
