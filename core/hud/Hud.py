import pygame

from core.PlayerInfo import PlayerInfo
from core.hud import font
from core.Player import Player

from pygame.locals import K_TAB

from core.hud.menu.ShipMenu import ShipMenu
from setting import *

class Hud():
    
    def __init__(self) -> None:
        
        self.player = None 
        self.display_surface = pygame.display.get_surface()
        self.primary_font = font.get_primary_font()

        self.menus = {
            ShipMenu.__name__: ShipMenu(K_TAB)
        }        
    
    def draw(self):
        
        basic_player_info = PlayerInfo.get_player_ship_basic_info(self.player)
        self.draw_power(basic_player_info)
        self.draw_menus()

    def draw_power(self, info) -> pygame.surface.Surface:

        value = formatted_value = "Power: {:.2f} Vz".format(info["power"])

        surface = self.primary_font.render(value, None, HUD_CONFIG["POWER"][HUD_COLOR]) 
        self.display_surface.blit(surface, HUD_CONFIG["POWER"][HUD_POSITION])
        
    def update_menus(self):
        for k in self.menus:
            self.menus[k].update()
            
    def draw_menus(self):
        for k in self.menus:
            self.menus[k].draw()
            
    def set_player(self, player: Player):
        self.player = player
        
    def update(self, *args, **kargs):
        self.update_menus()
        