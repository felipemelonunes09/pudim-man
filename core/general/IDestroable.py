

from abc import ABCMeta, abstractmethod


class IDestroable(metaclass=ABCMeta):

    @abstractmethod
    def destroy(self):
        pass

