
from core.hud.menu.Menu import Menu
import pygame

class ShipMenu(Menu):
    
    menuConfig = {
        "Rooms": {
            "Power Room": None
        }
    }
    
    def get_interface(self) -> pygame.Surface:
        
        surface = self.get_surface()
        
        return surface

        