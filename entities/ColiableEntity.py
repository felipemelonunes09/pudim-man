from entities.Entity import Entity
from core.IColiable import IColiable


class ColiableEntity(Entity, IColiable):
    def __init__(self, walkRight: list, walkLeft: list, walkUp: list, walkDown: list):
        super().__init__(walkRight, walkLeft, walkUp, walkDown)
