import pygame
from core.Engine import Engine
from config import globals

from core.input.InputHandler import IInputHandler
from core.input.PCInputHandler import PCInputHandler
from core.input.AndroidInputHandler import AndroidInputHandler

def getInputHandlerFromPlataform(platform: int) -> IInputHandler:
    if platform == 1:
        return PCInputHandler()
    elif platform == 2:
        return AndroidInputHandler()
    else:
        raise ValueError("Invalid platform type")


if __name__ == "__main__":
    pygame.init()
    engine = Engine(inputHandler=getInputHandlerFromPlataform(globals.TARGET_DEVICE))
    engine.start()
    pygame.quit()