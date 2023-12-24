from abc import ABCMeta, abstractmethod


from core.general.ICollidable import ICollidable
from core.general.IDestroable import IDestroable

class IShot(ICollidable, IDestroable, metaclass=ABCMeta):
    pass