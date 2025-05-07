import os
##
## <!-- OS Globals --!>
##

# ! initial values may change depending on the plataform
TARGET_DEVICE       = 1                                     # 1 = pc, 2 = android
FPS                 = 60
SCREEN_SIZE         = (1500, 800)
SCREEN_COLOR        = (0, 0, 0)
SELECTED_TEXT_COLOR = (139, 119, 0) 
TEXT_COLOR          = "yellow"
FONT_SIZE           = 50
FONT                = None

##
## <!-- Path Globals --!>
##

PATH = os.path.abspath('.')+'/'

# harded coded paths 
ASSETS_IMAGE_DIR    = f"{PATH}assets/images"
PLAYER_IMAGE_DIR    = f"{ASSETS_IMAGE_DIR}/pudim/"
PAN_IMAGE_DIR       = f"{ASSETS_IMAGE_DIR}/pan/"
JELLY_IMAGE_DIR     = f"{ASSETS_IMAGE_DIR}/jelly/"

MAPS_DIR = f"{PATH}data/maps"
LEVEL_1 = f"{MAPS_DIR}/level_1.json"


BLOCK_SIZE = FONT_SIZE
SPRITE_SCALE_RATIO = (BLOCK_SIZE*0.8, BLOCK_SIZE*0.8)
BLOCK_COLOR = "blue"
POINT_COLOR = "yellow"
SPECIAL_COLOR = "white"



