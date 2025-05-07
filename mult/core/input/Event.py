from utils.helpers import Direction

class Event():
    pass

class UpdatePlayerPositionEvent(Event):
    def __init__(self, cardinalDirection: Direction):
        self.cardinalDirection = cardinalDirection
        super().__init__()