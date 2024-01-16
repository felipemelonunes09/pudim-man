
from typing import Any
from setting import *
import pygame

## this class contains an error
## cooldown does not storege previus usage of cooldown so it return to state 0 in both cases
class Cooldown(object):

    def __init__(self, cooldown, method, cooldown_callback=None) -> None:
                
        self.__cooldown = cooldown
        self.__colldown_callback = cooldown_callback
        self.__method = method
        self.__clock = pygame.time.Clock()


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if(self.__clock.tick() >= self.__cooldown):
            return self.__method(*args, **kwds)
        else: 
            if self.__colldown_callback is not None:
                return self.__colldown_callback(*args, **kwds)

        

    


