from core.input.InputHandler import IInputHandler
from core.input.Event import Event, UpdatePlayerPositionEvent
from utils.helpers import Direction
import pygame

class AndroidInputHandler(IInputHandler):

    def __init__(self):
        self.start_pos = None  # (x, y)

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

            min_distance = 0.05  # distância mínima para considerar swipe

            if abs(dx) > abs(dy) and abs(dx) > min_distance:
                if dx > 0:
                    print("[Swipe Detected] Direction: RIGHT")
                    return UpdatePlayerPositionEvent(Direction.RIGHT)
                else:
                    print("[Swipe Detected] Direction: LEFT")
                    return UpdatePlayerPositionEvent(Direction.LEFT)
            elif abs(dy) > min_distance:
                if dy > 0:
                    print("[Swipe Detected] Direction: DOWN")
                    return UpdatePlayerPositionEvent(Direction.DOWN)
                else:
                    print("[Swipe Detected] Direction: UP")
                    return UpdatePlayerPositionEvent(Direction.UP)

            print("[Swipe Ignored] Movement too small.")
            self.start_pos = None

        return None