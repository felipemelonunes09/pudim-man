import pygame
from core.Engine import Engine
from config import globals

from core.input.InputHandler import IInputHandler
from core.input.PCInputHandler import PCInputHandler
from core.input.AndroidInputHandler import AndroidInputHandler

def getInputHandlerFromPlataform(platform: globals.Platform) -> IInputHandler:
    if platform == globals.Platform.PC:
        return PCInputHandler()
    elif platform == globals.Platform.ANDROID:
        return AndroidInputHandler()
    else:
        raise ValueError("Invalid platform type")

if __name__ == "__main__":
    pygame.init()
    engine = Engine(inputHandler=getInputHandlerFromPlataform(globals.TARGET_DEVICE))
    engine.start()
    pygame.quit()