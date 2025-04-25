import pygame
import os
from config import globals
from core.StateManager import StateManager
from core.screen.Screen import Screen

class MenuScreen(Screen):
    def __init__(self, *args, **kwargs):
        self.font = pygame.font.SysFont("Arial", globals.FONT_SIZE)
        self.currentList = self.readLevels()
        self.options = [{
            "text": "Play"
        },
        {
            "text": "Options"
        },
        {
            "text": "Exit  "
        }
        ]

        super().__init__(initialState=StateManager.State.ON_MENU, *args, **kwargs)

    def getSurface(self) -> pygame.Surface:
        
        surface = pygame.Surface(globals.SCREEN_SIZE)
        surface.fill("white")
        match self.state.getState():
            case StateManager.State.ON_MENU:
                spacing = 60
                total_height = len(self.menuItens) * self.font.get_height() + (len(self.menuItens) - 1) * spacing
                start_y = (globals.SCREEN_SIZE[1] - total_height) // 2

                for i, item in enumerate(self.menuItens):
                    text_surface = self.font.render(item, True, "black")
                    text_rect = text_surface.get_rect(center=(globals.SCREEN_SIZE[0] // 2, start_y + i * (self.font.get_height() + spacing)))
                    surface.blit(text_surface, text_rect)

        return surface
    
    def readLevels(self):
        return [f for f in os.listdir(globals.MAPS_DIR) if os.path.isfile(os.path.join(globals.MAPS_DIR, f))]
