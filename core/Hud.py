import pygame
from core.PlayerInfo import PlayerInfo

from setting import *
from core.Player import Player


class Hud():
    
    def __init__(self) -> None:
        self.player = None
        self.display_surface = pygame.display.get_surface()
        self.primary_font = pygame.font.Font(HUD_PRIMARY_FONT_PATH, HUD_PRIMARY_FONT_SIZE)
        self.primary_font.bold = True

    def update(self):
        if self.player is not None:

            basic_player_info = PlayerInfo.get_player_ship_basic_info(self.player)
            
            self.handle_speed(basic_player_info)



    def handle_speed(self, info) -> pygame.surface.Surface:

        value = formatted_value = "Velocity: {:.2f}%".format(info["speed"] * 100)

        surface = self.primary_font.render(value, None, HUD_CONFIG["SPEED"][HUD_COLOR]) 
        self.display_surface.blit(surface, HUD_CONFIG["SPEED"][HUD_POSITION])

    def set_player(self, player: Player):
        self.player = player
    



    