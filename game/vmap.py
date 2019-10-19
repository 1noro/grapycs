#game.map
#by boot1110001

### IMPORTS ####################################################################
import pygame

def crete_base_map(vsqW, vsqH):
    out = []
    i = 0
    while i < vsqH:
        out.append([])
        e = 0
        while e < vsqW:
            out[i].append(0)
            e += 1
        i += 1
    return out



### CLASSES ####################################################################
class VMap:
    def __init__(self, vsqW, vsqH):
        self.vsqW = vsqW
        self.vsqH = vsqH
        self.vmap = []
        i = 0
        while i < vsqH:
            self.vmap.append([])
            e = 0
            while e < vsqW:
                self.vmap[i].append(0)
                e += 1
            i += 1

    def draw(self, screen):
        pass

    def __eq__(self,other):
        out=False
        return out
