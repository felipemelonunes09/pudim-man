from entities.Entity import Entity
from core.IColiable import IColiable
from scenes.Tile import Tile


class ColiableEntity(Entity, IColiable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def onCollision(self, entity: Entity):
        if isinstance(entity, Tile):
            self.rect.x = self.lastX
            self.rect.y = self.lastY

        return super().onCollision(entity)