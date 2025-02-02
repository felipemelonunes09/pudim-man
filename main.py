import pygame
from core.Engine import Engine

if __name__ == "__main__":
    pygame.init()
    engine = Engine()
    engine.start()
    pygame.quit()