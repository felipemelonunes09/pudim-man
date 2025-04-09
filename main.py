import pygame
from core.Engine import Engine

if __name__ == "__main__":
    pygame.init()

    icon = pygame.image.load("./assets/images/pudim/eat/0.png")

    pygame.display.set_icon(icon)
    pygame.init()
    engine = Engine()
    engine.start()
    pygame.quit()