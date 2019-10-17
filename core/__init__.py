#core.__init__
#by boot1110001

### IMPORTS ####################################################################
import sys, os, re
import getopt
from optparse import OptionParser
# To not show the default message of pygame import
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

from graphic.color import stdCs
# from graphic import displays
from graphic.elements.rectangle import Rectangle
from graphic.elements.sq_rectangle import SQRectangle
from graphic.elements.sq_square import SQSquare

from graphic.gameElements.arrow_map import ArrowMap

import languages
from languages import *

### EDITABLE VARIABLES #########################################################
lang = en.EN
verbose = True

sqpx = 23 # 10/15/40... (square size in px) (stdsize)
vsqW = 31 # ODD NUMBER def=15 (number of visible squares WIDTH) (cellscope)
vsqH = 31 # ODD NUMBER def=15 (number of visible squares HEIGHT) (cellscope)

### AUTOMATIC VARIABLES ########################################################
vsqpxW = sqpx * vsqW # number of visible squares WIDTH in px (pxscope)
vsqpxH = sqpx * vsqH # number of visible squares HEIGHT in px (pxscope)
sqcenterW = int((vsqW / 2) + 0.5) # screen square center WIDTH (cellcenter)
sqcenterH = int((vsqH / 2) + 0.5) # screen square center HEIGHT (cellcenter)
pxcenterW = (vsqpxW / 2) - (vsqpxW / 2) # screen pixel center WIDTH (pxcenter)
pxcenterH = (vsqpxH / 2) - (vsqpxH / 2) # screen pixel center HEIGHT (pxcenter)

psv = python_short_version = re.compile(r'([0-9]\.[0-9])\.[0-9] ').match(sys.version).group(1)

### NON EDITABLE VARIABLES #####################################################
# --- Files and folders
main_pkg = 'core'
version_file = 'version.txt'
icon_file = 'media/icon.ico'
# icon_file = 'media/icon.png'
font_file = 'media/node.ttf'

### FUNCTIONS ##################################################################


### MAIN #######################################################################
def main():
    # --- GLOBAL VARIABLES -----------------------------------------------------
    global verbose, lang, version_file, icon_file, font_file

    # --- MAIN VARIABLES -------------------------------------------------------
    width, height = vsqpxW, vsqpxH # window size

    # --- state control
    # 0 - menu
    # 1 - game
    # 2 - ...
    # 3 - game config
    # 4 - credits
    screen = 0

    # --- version variables
    version = ""
    shortversion = ""
    try:
        version = open(version_file, 'r').read().replace('\n','')
        patron = re.compile(r'(.*\..*\..*)\.')
        shortversion = patron.search(version).group(1)
    except:
        print(lang.version_warning)

    # --- CMD INIT -------------------------------------------------------------
    print(lang.wellcome_msg+version+")")
    print(lang.wellcome_info+pygame.version.ver+")")

    # --- Parameters -----------------------------------------------------------
    parser = OptionParser()
    parser.add_option(
        "-v", "--verbose", dest="verbose",
        action="store_true", default=False,
        help="print status messages to stdout.")
    parser.add_option(
        "-l", "--lang", dest="lang",
        help="changes the default language."
    )

    (options, args) = parser.parse_args()

    # --- Verbose
    verbose = options.verbose

    # --- Language
    if options.lang:
        lang = languages.set_lang(options.lang)

    # --- PYGAME INIT ----------------------------------------------------------
    pygame.init()
    # Set the height and width of the screen
    size = [width, height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("GRAPYCS " + shortversion)
    logo = pygame.image.load(icon_file)
    pygame.display.set_icon(logo)
    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------------------------------------------
    while not done:
        # --- Event Processing & logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # pygame.quit()

        # --- Drawing
        # SQRectangle(1, 1, 1, 2, sqpx, stdCs.LIGHT_BLUE).draw(screen)
        # SQSquare(1, 3, 1, sqpx, stdCs.STAR_CMD_BLUE).draw(screen)
        ArrowMap(1, 1, sqpx).draw(screen)

        # --- Wrap-up
        clock.tick(60) # Limit to 60 frames per second

        pygame.display.flip()

    # Close everything down
    pygame.quit()
