from core.input.InputHandler import IInputHandler
from core.input.Event import Event, DirectionInputEvent, PointInputEvent
from utils.helpers import Direction
import pygame

class PCInputHandler(IInputHandler):

    def __init__(self):
        pass

    def translateEvent(self, event: pygame.event) -> Event:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return DirectionInputEvent(Direction.UP)
            elif event.key == pygame.K_DOWN:
                return DirectionInputEvent(Direction.DOWN)
            elif event.key == pygame.K_LEFT:
                return DirectionInputEvent(Direction.LEFT)
            elif event.key == pygame.K_RIGHT:
                return DirectionInputEvent(Direction.RIGHT)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return PointInputEvent(position=event.pos)
        return None