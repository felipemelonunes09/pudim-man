from typing import Tuple
from utils.helpers import Direction

class Event():
    pass

class DirectionInputEvent(Event):
    def __init__(self, cardinalDirection: Direction):
        self.cardinalDirection = cardinalDirection
        super().__init__()


class PointInputEvent(Event):
    def __init__(self, position: Tuple[int, int]):
        self.position = position
        super().__init__()