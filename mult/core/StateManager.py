from __future__ import annotations
from enum import Enum

class StateManager():
    class State(Enum):
        ## < Common States >
        EXITING = -1
        DEFAULT = 0

        ## < Menu States >
        ON_MENU=10
        ON_MENU_CONFIG=11
        ON_MENU_LEVELS=12

        RUNNING = 20
        QUESTIONING = 21
        ENDGAME = 22
        
    def __init__(self, state: State):
        self.__state = state

    def getState(self) -> State:
        return self.__state
    
    def setState(self, state: State):
        self.__state = state

