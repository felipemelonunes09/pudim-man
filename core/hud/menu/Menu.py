import pygame

from core.hud import font
from setting import *

from abc import abstractmethod


class Menu():
        
    def __init__(self, 
        key_activation,
        width = SCREEN_WIDTH - HUD_MENU_MARGIN,
        height = SCREEN_HEIGHT - HUD_MENU_MARGIN,
        x = HUD_MENU_MARGIN / 2,
        y = HUD_MENU_MARGIN / 2,
        color = HUD_MENU_COLOR,
        alpha = HUD_MENU_ALPHA
        
    ) -> None:
        
        self.display = False
        self.key_activation = key_activation
        self.display_surface = pygame.display.get_surface()
        
        self.primary_font = font.get_primary_font()
        
        self.width = width
        self.height = height
        
        self.x = x
        self.y = y
        
        self.color = color
        self.alpha = alpha
        
            
    def update(self, *args, **kwargs):
        pressedkeys = pygame.key.get_pressed()
        if pressedkeys[self.key_activation]:
            self.display = True
        else:
            self.display = False

    
    def draw(self):
        if self.display:
            surface = self.get_interface()
            correction = HUD_MENU_MARGIN/2
            self.display_surface.blit(surface, (self.x, self.y))
            
    def get_surface(self) -> pygame.Surface:
        
        surface = pygame.Surface((self.width, self.height))
        surface.fill(self.color)
        surface.set_alpha(self.alpha)
        
        return surface
    
    def flip(self):
        self.display = not self.display
        
    @abstractmethod
    def get_interface() -> pygame.Surface:
        pass
    