import pygame
from setting import *

## review this method
def get_primary_font(bold = True):
    primary_font = pygame.font.Font(HUD_PRIMARY_FONT_PATH, HUD_PRIMARY_FONT_SIZE)
    primary_font.bold = bold
    
    return primary_font
