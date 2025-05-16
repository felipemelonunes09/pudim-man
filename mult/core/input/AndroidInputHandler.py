from typing import Tuple
from core.input.InputHandler import IInputHandler
from core.input.Event import Event, DirectionInputEvent, PointInputEvent
from utils.helpers import Direction
import pygame

class AndroidInputHandler(IInputHandler):

    def __init__(self):
        self.start_pos: Tuple[int, int] = None  # (x, y)

    def translateEvent(self, event: pygame.event) -> Event:
        if event.type == pygame.FINGERDOWN:
            self.start_pos = (event.x, event.y)
            print(f"[Swipe Start] Position: {self.start_pos}")

        elif event.type == pygame.FINGERUP and self.start_pos:
            end_pos = (event.x, event.y)
            print(f"[Swipe End] Position: {end_pos}")

            dx = end_pos[0] - self.start_pos[0]
            dy = end_pos[1] - self.start_pos[1]
            print(f"[Swipe Delta] dx: {dx:.4f}, dy: {dy:.4f}")

            min_swipe_distance = 0.05  
            max_tap_distance = 0.01   

            if abs(dx) <= max_tap_distance and abs(dy) <= max_tap_distance:
                print("[Tap Detected] Single tap recognized.")
                return PointInputEvent(position=(end_pos[0], end_pos[1])) 

            if abs(dx) > abs(dy) and abs(dx) > min_swipe_distance:
                if dx > 0:
                    print("[Swipe Detected] Direction: RIGHT")
                    return DirectionInputEvent(Direction.RIGHT)
                else:
                    print("[Swipe Detected] Direction: LEFT")
                    return DirectionInputEvent(Direction.LEFT)
            elif abs(dy) > min_swipe_distance:
                if dy > 0:
                    print("[Swipe Detected] Direction: DOWN")
                    return DirectionInputEvent(Direction.DOWN)
                else:
                    print("[Swipe Detected] Direction: UP")
                    return DirectionInputEvent(Direction.UP)

            print("[Swipe Ignored] Movement too small.")
            self.start_pos = None

        return None
