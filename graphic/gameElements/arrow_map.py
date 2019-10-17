#graphic.gameElements.arrow_map
#by boot1110001

### IMPORTS ####################################################################
from ..color import stdCs
from ..elements.sq_square import SQSquare

### CLASSES ####################################################################
class ArrowMap:
    def __init__(self, sqx, sqy, sqpx):
        self.sqpx = sqpx
        self.sqx = sqx
        self.sqy = sqy

    def draw(self, screen, active):
        # active:
        # 0 - none
        # 1 - up
        # 2 - left
        # 3 - down
        # 4 - right
        switch (active):
            case 1:
                SQSquare(self.sqx+1, self.sqy, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
                SQSquare(self.sqx, self.sqy+1, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
                SQSquare(self.sqx+1, self.sqy+1, 1, self.sqpx, stdCs.STAR_CMD_BLUE).draw(screen)
                SQSquare(self.sqx+2, self.sqy+1, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
                break
            case 1:
                SQSquare(self.sqx+1, self.sqy, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
                SQSquare(self.sqx, self.sqy+1, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
                SQSquare(self.sqx+1, self.sqy+1, 1, self.sqpx, stdCs.STAR_CMD_BLUE).draw(screen)
                SQSquare(self.sqx+2, self.sqy+1, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
            case 1:
                SQSquare(self.sqx+1, self.sqy, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
                SQSquare(self.sqx, self.sqy+1, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
                SQSquare(self.sqx+1, self.sqy+1, 1, self.sqpx, stdCs.STAR_CMD_BLUE).draw(screen)
                SQSquare(self.sqx+2, self.sqy+1, 1, self.sqpx, stdCs.LIGHT_BLUE).draw(screen)
