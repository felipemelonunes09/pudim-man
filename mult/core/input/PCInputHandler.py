from core.input.InputHandler import IInputHandler
from core.input.Event import Event, UpdatePlayerPositionEvent
from utils.helpers import Direction
import pygame

class PCInputHandler(IInputHandler):

    def __init__(self):
        pass

    def translateEvent(self, event: pygame.event) -> Event:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return UpdatePlayerPositionEvent(Direction.UP)
            elif event.key == pygame.K_DOWN:
                return UpdatePlayerPositionEvent(Direction.DOWN)
            elif event.key == pygame.K_LEFT:
                return UpdatePlayerPositionEvent(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                return UpdatePlayerPositionEvent(Direction.RIGHT)
        return None